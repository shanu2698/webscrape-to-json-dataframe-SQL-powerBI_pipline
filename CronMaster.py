from apscheduler.schedulers.blocking import BlockingScheduler
from pandas.io.json import json_normalize
import DataFrame_MySQL as dm
import dummy_customer as dco
import TwitterScrape as tso
import dummy_order as doo
import Flipkart as fso
import Cleaner as co
import pandas as pd
import datetime
import pyodbc
import time
import json

def job_tasks():

    startTime = time.time()
    flipkart_Json = fso.get_ScrapFlipkartData() #retreiving data
    twitter_Json = tso.get_ScrapeTweetData() #retreiving data

    customer_Dataframe = dco.get_customer_details() #retreiving data
    order_Dataframe = doo.get_order_details() #retreiving data

    product_Dataframe = pd.read_csv('product.csv')
    

    flipkart_Dict = json.loads(flipkart_Json)
    twitter_Dict = json.loads(twitter_Json)

    flipkart_Dataframe = pd.json_normalize(flipkart_Dict) #Json to DataFrame / Table
    #print(flipkart_Dataframe.head())
    twitter_Dataframe = pd.json_normalize(twitter_Dict) #Json to DataFrame / Table
    #print(twitter_Dataframe.head())

    cleaned_flipkart_Dataframe = co.CleaningProcedure(flipkart_Dataframe)  #cleaning_data
    cleaned_twitter_Dataframe =  co.CleaningProcedure(twitter_Dataframe)   #cleaning_data

    #cleaned_flipkart_Dataframe.to_csv("Flipkart Data.csv", index = False)
    #cleaned_twitter_Dataframe.to_csv("Twitter Data.csv", index = False)
    #customer_Dataframe.to_csv("Customer Details Data.csv", index = False)
    #order_Dataframe.to_csv("Order Details Data.csv", index = False)


    con = dm.get_connection()
    
    dm.Push_to_MySQL(cleaned_flipkart_Dataframe,'flipkart_table',con)
    dm.Push_to_MySQL(cleaned_twitter_Dataframe,'twitter_table',con)
    dm.Push_to_MySQL(customer_Dataframe,'customer_details_table',con)
    dm.Push_to_MySQL(order_Dataframe,'order_details_table',con)
    dm.Push_to_MySQL(product_Dataframe,'product_details_table',con)

    print("Commands sent successfully...... \nFirst execution completed successfully!\nExecution time: ",time.time()-startTime, 'seconds')


scheduler = BlockingScheduler()
scheduler.add_job(job_tasks, 'interval', minutes=30, next_run_time=datetime.datetime.now())
scheduler.start()
