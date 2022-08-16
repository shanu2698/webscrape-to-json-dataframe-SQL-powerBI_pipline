import snscrape.modules.twitter as sntwitter
import pandas as pd
import misc as mo
import json

#SearchList = ['#Nothingphone1 since:2022-07-04 until:2022-07-20 min_faves:5','#OPPOReno8 since:2022-07-17 until:2022-08-02 min_faves:5','#POCOF45G since:2022-06-19 until:2022-07-08 min_faves:5']

SearchList = ['#Nothingphone1 since:2022-07-04 until:2022-07-20','#OPPOReno8 since:2022-07-17 until:2022-08-02','#POCOF45G since:2022-06-19 until:2022-07-08']

def ScrapeTweets(element):
    tempList = []
    try:
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(SearchList[element]).get_items()):
            if i>10000:
                break
            dict = {'UserName': str(tweet.user.username),
                    'Date': str(tweet.date),
                    'LikeCount': str(tweet.likeCount),
                    'Source': str(tweet.sourceLabel),
                    'Comment': str(tweet.content),
                    'Brand': str(SearchList[element][1:-34])
                    }
            tempList.append(dict)
    except:
        return tempList
    return tempList

    
def get_ScrapeTweetData():
    tweetData = []
    for element in range(3):
        temp = ScrapeTweets(element)
        tweetData.append(temp)
    TweetData = mo.FlattenList(tweetData)

    TweetData_JSON = json.dumps(TweetData,indent = 4)
    return TweetData_JSON

"""
myJSON = get_ScrapeTweetData()

with open('TwitterData.json', 'w') as file:
    file.write(myJSON)

"""