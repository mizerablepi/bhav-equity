import requests
import os
import shutil
import glob
import pandas as pd
import sqlite3

#TASK a: Automate downloading of bhav copy files (equity) from BSE India Website for month of May 2023 
URL = "https://www.bseindia.com/download/BhavCopy/Equity/"
MONTH = '05' #Change this to required month accordingly
YEAR = '23' #Change this to required year accordingly

headers = {
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101'
}

for i in range(1,32):
  file = f'EQ{i:02d}{MONTH}{YEAR}_CSV.ZIP'
  r = requests.get(URL+file,headers = headers)
  if r.status_code == 404:
    continue;
  f = open('data/'+file.lower(),"wb")
  f.write(r.content)
  f.close()

for file in os.listdir('data/'):
  shutil.unpack_archive(f'data/{file}', 'csv/')

#TASK b: Upload the files into SQL database in one table (all files of equity for May 2023)  
path = 'csv/'
csv_files = glob.glob(path + '/*.CSV')
df = pd.concat(map(pd.read_csv, csv_files))

conn = sqlite3.connect('bhav.db')
cursor = conn.cursor()

df.to_sql('may_equity', conn, if_exists='append', index = False)

conn.close()