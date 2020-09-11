import pandas as pd
import glob,json,math

df=pd.read_csv(r'E:\Study\Dalhousie\DM\Assignment 4\News\cleaned_news_data.csv',encoding= 'unicode_escape')

for i in range(len(df['title'])):
    temp_dict={
        'title':df['title'][i],
        'description':df['description'][i],
        'content':df['content'][i]
    }
    f=open(r'E:\Study\Dalhousie\DM\Assignment 4\News\News Articles\{0}_news_article'.format(i),'w')
    f.write(str(temp_dict))
    f.close()

no_of_articles=100
keywords=['canada','university','dalhousie university','halifax','business']
keywords_count=[0,0,0,0,0]
canada_in=[]
flag=0
for article in glob.glob(r'E:\Study\Dalhousie\DM\Assignment 4\News\News Articles\*'):
    f=open(article,'r')
    temp_dict=eval(f.read())
    for index,keyword in enumerate(keywords):
        if keyword in temp_dict['title'].lower():
            if keyword=='canada':
                canada_in.append(article)
            keywords_count[index]+=1
        elif keyword in temp_dict['description'].lower():
            if keyword=='canada':
                canada_in.append(article)
            keywords_count[index]+=1
        elif keyword in temp_dict['content'].lower():
            if keyword=='canada':
                canada_in.append(article)
            keywords_count[index]+=1
print(keywords_count)
df_N=[100/i for i in keywords_count]
log_10=[math.log10(i) for i in df_N]
print(keywords)
print(keywords_count)
print(df_N)
print(log_10)
df_dict={
    'Keyword':keywords,
    'df':keywords_count,
    'N/df':df_N,
    'log10(N/df)':log_10
}
df=pd.DataFrame(df_dict,columns=['Keyword','df','N/df','log10(N/df)'])
df.to_csv(r'E:\Study\Dalhousie\DM\Assignment 4\News\10.a.csv',index=False,header=True)
freq_in_article=[]
total_words=[]
for article in canada_in:
    count=0
    words=0
    f=open(article,'r')
    temp_dict=eval(f.read())
    words+=len(temp_dict['title'].split())
    if 'canada' in temp_dict['title'].lower():
        count+=temp_dict['title'].lower().count('canada')
    words+=len(temp_dict['description'].split())
    if 'canada' in temp_dict['description'].lower():
        count+=temp_dict['description'].lower().count('canada')
    words+=len(temp_dict['content'].split())
    if 'canada' in temp_dict['content'].lower():
        count+=temp_dict['content'].lower().count('canada')
    total_words.append(words)
    freq_in_article.append(count)
f_m=[freq_in_article[i]/total_words[i] for i in range(len(freq_in_article))]
freq_dict={
    'Article':canada_in,
    'Total_words':total_words,
    'frequency':freq_in_article,
    'relative_freq':f_m
}
df=pd.DataFrame(freq_dict,columns=['Article','Total_words','frequency','relative_freq'])
df.to_csv(r'E:\Study\Dalhousie\DM\Assignment 4\News\relative_frequency.csv',index=False,header=True)
index=f_m.index(max(f_m))#get index of the article with most relative frequency
print("Article with highest relative frequency is {0}".format(canada_in[index].split('\\')[-1]))