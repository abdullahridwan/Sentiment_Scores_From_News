
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st


@st.cache
def sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    #print("Overall sentiment dictionary is : ", sentiment_dict)
    #print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    #print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    #print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

    res = ""
    if sentiment_dict['compound'] >= 0.05:
        res= "Positive"

    elif sentiment_dict['compound'] <= - 0.05:
        res= "Negative"

    else:
        res= "Neutral"
    
    #print("Sentence Overall Rated As " + res)
    return res