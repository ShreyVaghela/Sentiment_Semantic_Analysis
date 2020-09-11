import pandas as pd
df=pd.read_csv(r'E:\Study\Dalhousie\DM\Assignment 4\Twitter\cleaned_twitter_data.csv',encoding= 'unicode_escape')
list=[]
pos_words=[]
neg_words=[]
pos_matched_words=[]
neg_matched_words=[]
polarity=[]
f=open('E:\Study\Dalhousie\DM\Assignment 4\Twitter\positive_words.txt','r')
for word in f:
	pos_words.append(word.strip('\n').lower())

f.close()
f=open(r'E:\Study\Dalhousie\DM\Assignment 4\Twitter\negative_words.txt','r')
for word in f:
	neg_words.append(word.strip('\n').lower())



for index,row in df.iterrows():
	pos_count=0
	neg_count=0
	split_tweet=row['text'].split()
	for word in split_tweet:
		if word.lower() in pos_words:
			pos_matched_words.append(word.lower())
			pos_count+=1
		elif word.lower() in neg_words:
			neg_matched_words.append(word.lower())
			neg_count+=1
	if pos_count>neg_count:
		polarity.append('positive')
	elif neg_count>pos_count:
		polarity.append('negative')
	else:
		polarity.append('neutral')

df["polarity"]=polarity	
combine_words=[]
combine_freq=[]
combine_polarity=[]
for word in set(pos_matched_words):
	combine_words.append(word)
	combine_freq.append(pos_matched_words.count(word))
	combine_polarity.append('positive')

for word in set(neg_matched_words):
	combine_words.append(word)
	combine_freq.append(neg_matched_words.count(word))
	combine_polarity.append('negative')
data=[[combine_words[i],combine_freq[i],combine_polarity[i]]for i in range(len(combine_words))]
new_df=pd.DataFrame(data=data,columns=['words','frequency','polarity'])
df.to_csv(r'E:\Study\Dalhousie\DM\Assignment 4\Twitter\twitter_data_polarity.csv',index=False,header=True)
new_df.to_csv(r'E:\Study\Dalhousie\DM\Assignment 4\Twitter\words_polarity.csv',index=False,header=True)