import re
import string

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer

from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms

import numpy as np 

def handle_negations(tweet):
    negation_words = set(['not', 'no', 'never', 'none', 'neither', 'nor'])

    for i in range(len(tweet)):
        if tweet[i] in negation_words and i + 1 < len(tweet):
           
            tweet[i + 1] = 'not_' + tweet[i + 1]

    return tweet

def process_tweet(tweet):
    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english')

    tweet = re.sub(r'\$\w*', '', tweet)
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub(r'https?://[^\s\n\r]+', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True, reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and
                word not in string.punctuation):
            stem_word = stemmer.stem(word)
            tweets_clean.append(stem_word)

    # Ajouter l'appel à handle_negations ici
    tweets_clean = handle_negations(tweets_clean)

    # Vérifier si le mot "not" est présent
    not_present = 'not' in tweets_clean
    
    return tweets_clean, not_present







def lookup(freqs, word, label):
    
    n = 0  

    pair = (word, label)
    if (pair in freqs):
        n = freqs[pair]

    return n




def confidence_ellipse(x, y, ax, n_std=3.0, facecolor='none', **kwargs):
    
    if x.size != y.size:
        raise ValueError("x and y must be the same size")

    cov = np.cov(x, y)
    pearson = cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1])
   
    ell_radius_x = np.sqrt(1 + pearson)
    ell_radius_y = np.sqrt(1 - pearson)
    ellipse = Ellipse((0, 0),
                      width=ell_radius_x * 2,
                      height=ell_radius_y * 2,
                      facecolor=facecolor,
                      **kwargs)

   
    scale_x = np.sqrt(cov[0, 0]) * n_std
    mean_x = np.mean(x)

    
    scale_y = np.sqrt(cov[1, 1]) * n_std
    mean_y = np.mean(y)

    transf = transforms.Affine2D() \
        .rotate_deg(45) \
        .scale(scale_x, scale_y) \
        .translate(mean_x, mean_y)

    ellipse.set_transform(transf + ax.transData)
    return ax.add_patch(ellipse)

