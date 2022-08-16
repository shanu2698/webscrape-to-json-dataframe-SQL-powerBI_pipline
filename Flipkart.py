from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time, urllib.request
import FlipkartExtractor as FE
from time import sleep
import misc as mo
import requests
import json


def ScrapFlipkartData(num):

    chrome_options = Options()
    chrome_options.headless = True# to pop
    chrome_options.add_experimental_option("detach", True)

    PATH = (r"chromedriver.exe")
    driver = webdriver.Chrome(PATH, options = chrome_options )


    driver.get("https://www.flipkart.com/")
    time.sleep(3)

    html = driver.find_element(By.TAG_NAME,'html')
    html.send_keys(Keys.ESCAPE)
    searchbox = driver.find_element(By.CSS_SELECTOR,"input[name='q']")
    searchbox.clear()
    searchbox.send_keys(mo.product_Name[num])
    searchbox.send_keys(Keys.ENTER)
    time.sleep(3)

    product_link = driver.find_element(By.CSS_SELECTOR,"div._2kHMtA > a").get_attribute('href')
    driver.get(product_link)
    time.sleep(3)

    html = driver.find_element(By.TAG_NAME,'html')
    html.send_keys(Keys.ESCAPE)
    html.send_keys(Keys.END)
    time.sleep(6)
    
    
    
    try:
        select_all_reviews_link = driver.find_element(By.XPATH,mo.product_Xpath[num]).get_attribute('href')
    except:
        select_all_reviews_link =  mo.product_all_review_links[num]

    driver.close()

    no_of_pages = FE.getPageCount(select_all_reviews_link)
    data2 = []
    i = 1
    
    for eachPage in range(no_of_pages):
        temp1 = select_all_reviews_link + "&page=" + str(i)
        temp2 = FE.Extractfunc(temp1, num)
        data2.append(temp2)
        i = i+1


    Product_data_list = mo.FlattenList(data2)  
    return Product_data_list



def get_ScrapFlipkartData():
    Combined_Product_Data_list = []
    for x in range(3):
        temp = ScrapFlipkartData(x)
        Combined_Product_Data_list.extend(temp)

    data_JSON = json.dumps(Combined_Product_Data_list,indent = 4)
    return data_JSON


"""
myJSON = get_ScrapFlipkartData()

with open('finalData.json', 'w') as file:
    file.write(myJSON)
"""

