from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pandas as pd
import misc as mo
import nltk
import re

#nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def CleaningProcedure(dataframe):
  Comments = dataframe['Comment']
  Comments = Comments.to_list()
  cleaned = []
  for comment in Comments:
    temp = comment.lower()
    temp = temp.encode('ascii', 'ignore').decode()
    temp = re.sub("@\S+", " ",temp)
    temp = re.sub("https*\S+", " ", temp)
    temp = temp.replace("#"," ")
    #temp = re.sub("#\S+", " ", temp)
    temp = re.sub(r'[^\w\s]', '', temp)
    temp = re.sub('\s{2,}', " ", temp)
    temp = mo.RemoveAllStopwords(temp)
    cleaned.append(temp)
  dataframe['Comment'] = cleaned


  return dataframe
