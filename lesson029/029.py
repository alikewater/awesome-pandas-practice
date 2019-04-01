import pandas as pd
import pyodbc
import sqlalchemy

connection = pyodbc.connect('DRIVER=(SQL SERVER);SERVER=(local);DATABASE=AdventureWorks;USER=sa;PASSWORD=123456')
engine = sqlalchemy.create_engine('mssql+pyodbc://sa:123456@(local)/AdventrueWorks?driver=SQL+Server')

query='select * from people'

df1 = pd.read_sql_query(query,connection)
df2 = pd.read_sql_query(query,engine)

print(df1)
print(df2)

