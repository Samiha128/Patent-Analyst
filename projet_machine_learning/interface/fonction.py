
import json
import time
from streamlit_lottie import st_lottie
import requests
import altair as alt
import pandas as pd
import plotly.express as px
import streamlit as st
import fonction
import base64
import streamlit as st
import plotly.express as px
from PIL import Image
from googletrans import Translator

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer






def load_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


df = px.data.iris()




def convert_to_df(sentiment):
    sentiment_dict = {'polarity': sentiment.polarity, 'subjectivity': sentiment.subjectivity}
    sentiment_df = pd.DataFrame(sentiment_dict.items(), columns=['metric', 'value'])
    return sentiment_df


def analyze_token_sentiment(sentence, target_lang='en'):
    translator = Translator()
    translated_sentence = translator.translate(sentence, dest=target_lang).text
    analyzer = SentimentIntensityAnalyzer()
    pos_list = []
    neg_list = []
    neu_list = []
    for i in translated_sentence.split():
        res = analyzer.polarity_scores(i)['compound']
        if res > 0.1:
            pos_list.append(i)
            pos_list.append(res)
        elif res <= -0.1:
            neg_list.append(i)
            neg_list.append(res)
        else:
            neu_list.append(i)
    result = {'positives': pos_list, 'negatives': neg_list, 'neutral': neu_list}
    return result


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


def get_img_as_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/jpeg;base64,{encoded_image}"