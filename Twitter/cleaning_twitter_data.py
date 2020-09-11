
# coding: utf-8

# In[61]:


import pandas as pd
import re
import pymongo
client = pymongo.MongoClient("mongodb://") 
db = client.data3
collection=db['twitter']

# In[89]:


#df=pd.read_csv(r'E:\Study\Dalhousie\DM\Assignment 3\twitter_data.csv',encoding= 'unicode_escape')
#df['text'][10]


# In[90]:


#for i in range(len(df['text'])):
#    df['text'][i]=re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b','', df['text'][i], flags=re.MULTILINE)


# In[92]:


#df['text'][281]


# In[93]:


#List=[]
#for i in range(len(df['text'])):
#	df['text'][i]=re.sub('[^A-Za-z0-9]+',' ', df['text'][i], flags=re.MULTILINE)
#	df['user_name'][i]=re.sub('[^A-Za-z0-9]+',' ', df['user_name'][i], flags=re.MULTILINE)
#	df['user_location'][i]=re.sub('[^A-Za-z0-9]+',' ', str(df['user_location'][i]), flags=re.MULTILINE)


# In[94]:


#df.to_csv(r'E:\Study\Dalhousie\DM\Assignment 3\cleaned_twitter_data.csv',index=False,header=True)
df=pd.read_csv(r'E:\Study\Dalhousie\DM\Assignment 3\Twitter\cleaned_twitter_data.csv',encoding= 'unicode_escape')
list=[]
for index,row in df.iterrows():
	dict={
	"created_at":row["created_at"],
	"text":row["text"],
	"user_name":row["user_name"],
	"user_location":row["user_location"],
	"retweet_count":row["retweet_count"],
	"favorite_count":row["favorite_count"]
	}
	list.append(dict)
collection.insert_many(list)
