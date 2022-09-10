import tweepy
import sys
import pandas as pd
import numpy as np 
import datetime

access_token = "1329783463168315399-cab33mEtOSMubQjVej4QLrR6v2q9N9"
access_token_secret="raJ1OOqkCHKc9MjSRS4hY0HOhqwVYougQYPtZARDmlXfL"
consumer_key="PzQOICabXVwcv1za3b9GUkOr6"
consumer_secret = "Mp5GLsTs7pyxZPF4S98x3FtmBBYGTxlhIZFuU0jsQAAWB9HVf5"

def print_Dataframe_tweets(tweets):
        
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        return df

        
class MyStreamListener(tweepy.StreamListener):  
    def __init__(self,api=None,max_tweet=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0  
        self. tweets=[]
        self.max_tweet=max_tweet
    def on_status(self,status):
        self.num_tweets += 1
        if self.max_tweet!=None:
            if self.num_tweets <= self.max_tweet:
                self.tweets.append(status)
                df=print_Dataframe_tweets(self.tweets)
                print(df.loc[[self.num_tweets-1]])
                return True
            
            else:
                return False
        else:
            self.tweets.append(status)
            df=print_Dataframe_tweets(self.tweets)
            print(df)
    def on_error(self,status_code):
        print(status_code)

class Mystream():
    def __init__(self,auth,Listener):
        self.stream=tweepy.Stream(auth = auth, listener=Listener)
        
    def Start_stream(self,keyword_list):
        self.stream.filter(track=keyword_list)

   
    
    

