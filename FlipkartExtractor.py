from bs4 import BeautifulSoup as bs
import time, urllib.request
from lxml import html
import requests
import misc as mo

def Extractfunc(link,num):
  page = requests.get(link)
  soup = bs(page.content, 'html.parser')
  def ExtraxtEachPage(row):
    
    # finding all rows within the block
    sub_row = row.find_all('div',attrs={'class':'row'})
       
    # extracting text from 1st and 2nd row
    rating = sub_row[0].find('div').text

    summary = sub_row[0].find('p').text
    
    review = sub_row[1].find_all('div')[2].text
     
    location = sub_row[3].find('p',attrs={'class':'_2mcZGG'}).find_all('span')[1].text
    location = "".join(location.split(",")[1:]).strip()

    date = sub_row[3].find_all('p',attrs={'class':'_2sc7ZR'})[1].text
    #date = mo.getDate(date)

    sub_row_2 = row.find_all('div',attrs={'class':'_1e9_Zu'})[0].find_all('span',attrs={'class':'_3c3Px5'})

    upvotes = sub_row_2[0].text

    downvotes = sub_row_2[1].text

    dict = {
            'Rating': str(rating),
            'Summary': str(summary),
            'Comment': str(review),
            'Location': str(location),
            'Date' : str(date),
            'Upvotes': str(upvotes),
            'Downvotes': str(downvotes),
            'Brand' : str(mo.product_Name[num])
            }
    return dict

  rows = soup.find_all('div',attrs={'class':'col _2wzgFH K0kLPL'})
  data = []

  for row in rows:
    x = ExtraxtEachPage(row)
    data.append(x)
    
  return data



def getPageCount(link2):
    review_page = requests.get(link2)
    tree = html.fromstring(review_page.content)
    temp = tree.xpath('//*[@id="container"]/div/div[3]/div/div/div[2]/div[13]/div/div/span[1]')[0].text
    PageCount = int(temp[10:])
    return PageCount
