import tweepy as tp
import pandas as pd

api_key=''
api_secret_key=''
access_token_key=''
access_secret_token_key=''

authentication=tp.OAuthHandler(api_key,api_secret_key)
authentication.set_access_token(access_token_key,access_secret_token_key)
api=tp.API(authentication,wait_on_rate_limit=True)

keywords="Canada OR University OR Dalhousie University OR Halifax OR Canada Education"
retrieved_tweets=tp.Cursor(api.search,q=keywords,lang="en").items(3100)
data=[[tweet.created_at,tweet.text,tweet.user.name,tweet.user.location,tweet.retweet_count,tweet.favorite_count]for tweet in retrieved_tweets]
print(data)

df=pd.DataFrame(data=data,columns=['created_at','text','user_name','user_location','retweet_count','favorite_count'])
df.to_csv('twitter_data.csv',index=True,header=True)