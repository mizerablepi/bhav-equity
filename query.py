import sqlite3

#TASK c: Run query on the table to compute the stock wise average (open, high, low and closing) price for the month of May 2023
# I have limited the output to 5 

conn = sqlite3.connect('bhav.db')
cursor = conn.cursor()
data = cursor.execute('''
select avg(OPEN), avg(HIGH), avg(LOW), avg(CLOSE) 
from may_equity
group by SC_NAME
limit 5;
''')
print('(avg(OPEN), avg(HIGH), avg(LOW), avg(CLOSE))')
for row in data:
  print(row)

conn.close()