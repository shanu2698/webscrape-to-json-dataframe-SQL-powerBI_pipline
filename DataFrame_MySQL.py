from sqlalchemy import create_engine
import pandas as pd
import misc as mo


def get_connection():
     temp = create_engine(url = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(mo.user,mo.password,mo.host,mo.port,mo.database))
     return temp


def Push_to_MySQL(dataFrame,table_name,engine):
     try:
          engine = get_connection()
          print(f"Connection to the {mo.host} for user {mo.user} created successfully.")
     except Exception as ex:
          print("Connection could not be made due to the following error: \n", ex)

     dataFrame.to_sql(table_name, engine, if_exists='replace')
