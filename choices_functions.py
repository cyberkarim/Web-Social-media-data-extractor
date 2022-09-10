import twitter_credentials
import Main_crawler
import tweepy
import sys
import pandas as pd
import numpy as np 
import os

def funct_choice_1(Keywords_list,Max_tweets):
    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    searched_tweets = [status for status in tweepy.Cursor(api.search, q=Keywords_list).items(Max_tweets)]
    df= Main_crawler.print_Dataframe_tweets(searched_tweets)
    outname = 'export_dataframe.csv'

    outdir = './Results'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fullname = os.path.join(outdir, outname)    

    df.to_csv(fullname, index = True, header=True)
def funct_choice_2(User_name,Max_tweets):
    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    tweetS=[]
    for tweet  in tweepy.Cursor(api.user_timeline, id=User_name).items(Max_tweets):
        tweetS.append(tweet)
    df= Main_crawler.print_Dataframe_tweets(tweetS)
    outname = 'export_dataframe_user.csv'

    outdir = './Results'
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    fullname = os.path.join(outdir, outname)   
    df.to_csv (fullname, index = True, header=True)
def funct_choice_3(Keywords_list,isLimited,Max_tweets=None):
    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY,twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    if(isLimited==0):
        try:
            Listener= Main_crawler.MyStreamListener()
            stream=Main_crawler.Mystream(api.auth,Listener)
            stream.Start_stream(Keywords_list)
        except KeyboardInterrupt:
            print("Stream interrompu !!")
            sys.exit(0)

                
    else:
        Listener= Main_crawler.MyStreamListener(max_tweet=Max_tweets)
        stream=Main_crawler.Mystream(api.auth,Listener)
        stream.Start_stream(Keywords_list)

#if __name__ == "__main__":
    #funct_choice_1(["corona"],20)
    #funct_choice_2("@WHO",20)
    #funct_choice_3(["corona"],1, 20)
    #funct_choice_3(["corona"],0)
