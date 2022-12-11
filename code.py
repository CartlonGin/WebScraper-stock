import requests
import pandas as pd
import json

#dates = '20221001' 
dates = [20221001, 20220901, 20220801, 20220701] #list(month)
stock_no = '8215' #the stock number you want to scrape

df = pd.DataFrame()
for date in dates:
    url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=jason&date=%s&stockNo=%s' %(date,stock_no)
    html = requests.get(url)
    stock_json = html.json()
    df2 = pd.DataFrame(data= stock_json['data'], columns= stock_json['fields'])
    df = df.append(df2, ignore_index=True)

# print(df)
df.to_excel("stock_sql_data.xlsx", sheet_name='%s' %stock_no)
print("%s Done" %stock_no)
