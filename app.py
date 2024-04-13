from flask import Flask, request, jsonify
import pickle
import re
import string
import nltk                                # Python library for NLP
from nltk.corpus import twitter_samples    # sample Twitter dataset from NLTK
from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming

from nltk.stem import WordNetLemmatizer    # module for Lemmatization

from nltk.tokenize import TweetTokenizer
nltk.download('wordnet')
nltk.download('omw-1.4')

test_string='I hate pizza because it was bad lie'

#################################################################
# Loading lr
with open('logistic_regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

#Loading vectorizer
with open('vectorizer.pkl', 'rb') as file:
    loaded_vectorizer = pickle.load(file)

#1st function
def process_tweet(tweet):
    lemmatizer = WordNetLemmatizer()
    stopwords_english = stopwords.words('english')
    # remove stock market tickers like $GE
    tweet = re.sub(r'\$\w*', '', tweet)
    # remove old style retweet text "RT"
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    # remove hyperlinks    
    tweet = re.sub(r'https?://[^\s\n\r]+', '', tweet)
    # remove hashtags
    # only removing the hash # sign from the word
    tweet = re.sub(r'#', '', tweet)
    # tokenize tweets
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and  # remove stopwords
                word not in string.punctuation):  # remove punctuation
            # tweets_clean.append(word)
            lemma_word = lemmatizer.lemmatize(word,pos='v')  # stemming word
            tweets_clean.append(lemma_word)

    return tweets_clean

#2nd function
def list_to_string(lst):
    return ' '.join(lst)
    
#1st function call
test_string=process_tweet(test_string)    
print(test_string)

#2nd function call
test_string=list_to_string(test_string)
print(test_string)

#vectorizer
test_vector=loaded_vectorizer.transform([test_string])
print(test_vector)
print(test_vector.shape)

#prediction
prediction = loaded_model.predict(test_vector)
print(prediction)

sentiment_mapping = {0:'Negative',1:'Positive'}
predicted_sentiment = sentiment_mapping[prediction[0]] 
print(predicted_sentiment)