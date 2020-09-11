import requests
import pandas as pd
keywords=['Canada',  'University',  'Dalhousie University', 'Halifax', 'Canada Education', 'Moncton', 'Toronto']
url = ('http://newsapi.org/v2/everything?q='+ ' OR '.join(keywords)+'&language=en&apiKey=YOUR-API-KEY&pageSize=100')

response = requests.get(url)
data=[[article['source']['name'],article['author'],article['title'],article['description'],article['publishedAt']]for article in response.json()['articles']]
df=pd.DataFrame(data=data,columns=['source_name','author','title','description','publishedAt'])
df.to_csv('news_data.csv',index=False,header=True)