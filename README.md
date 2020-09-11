# Sentiment_Semantic_Analysis
The project extratcs the data from Twitter and NEWS API to perform the semantic and sentiment analysis. It performs the sentiment analysis on Twitter data at `Twitter/cleaned_twitter_data` and semantic analysis on NEWS data at `News/News Articles`. The Twitter data was extracted with the help of [Tweepy](http://docs.tweepy.org/en/latest/getting_started.html). The NEWS API was extracted using [NEWS API](https://newsapi.org/).

### Sentiment Analysis
The `Twitter` folder contains scripts like `cleaning_twitter_data.py`, `twitter_data.py`,  etc., which helps to extract data using the API and pre-process it. For the pre-processing, it removes any metadata, URLs, and any special characters. The `polarity_twitter_data.py` counts the number of positive and negative words in order to find the polarity of the tweets. It performs it by converting the tweets into bag-of-words of comparing them with the list of positive and negative words. The below figure shows the visualization of word cloud for positive and negative words occuring in the tweets in [Tableau](https://www.tableau.com/products/desktop).

![Tableu](https://github.com/ShreyVaghela/Sentiment_Semantic_Analysis/blob/master/Twitter/word_cloud.png)
