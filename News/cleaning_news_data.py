import pandas as pd
import re
df=pd.read_csv(r'E:\Study\Dalhousie\DM\Assignment 3\News\news_data.csv',encoding= 'unicode_escape')

for i in range(len(df['title'])):
	df['content'][i]=re.sub('[^A-Za-z0-9]+',' ', str(df['content'][i]), flags=re.MULTILINE)
	df['title'][i]=re.sub('[^A-Za-z0-9]+',' ', str(df['title'][i]), flags=re.MULTILINE)
	df['description'][i]=re.sub('[^A-Za-z0-9]+',' ', str(df['description'][i]), flags=re.MULTILINE)


df.to_csv(r'E:\Study\Dalhousie\DM\Assignment 4\News\cleaned_news_data.csv',index=False,header=True)

