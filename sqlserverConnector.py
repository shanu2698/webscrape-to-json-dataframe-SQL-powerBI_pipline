import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import pyodbc
import socket
#conn = sqlalchemy.create_engine(f'mssql+pyodbc://BeastMachine/presentation?trusted_connection=yes&driver=SQL Server Native Client 11.0')
#conn = create_engine(url = "mssql+pyodbc://root3:Mysql127@127.0.0.1:3306/presentation&driver=SQL Server Native Client 11.0")

df = pd.read_csv('names.csv')


#engine = sqlalchemy.create_engine("mssql+pyodbc://root3:Mysql127@localhost:3306/presentation")
engine = create_engine("mssql+pyodbc://root3:Mysql127@BEASTMACHINE\SQLEXPRESS/presentation?driver=SQL+Server")


df.to_sql("table_name", engine,if_exists = "fail", index=False)

print("Command sent !!")
