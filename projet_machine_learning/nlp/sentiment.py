from utils import process_tweet, lookup
import pdb
from nltk.corpus import stopwords, twitter_samples
import numpy as np
import pandas as pd
import nltk
import string
from nltk.tokenize import TweetTokenizer
from os import getcwd


#nltk.download('twitter_samples')
#nltk.download('stopwords')

filePath = f"{getcwd()}/../tmp2/"
nltk.data.path.append(filePath)



all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')


test_pos = all_positive_tweets[4000:]
train_pos = all_positive_tweets[:4000]
test_neg = all_negative_tweets[4000:]
train_neg = all_negative_tweets[:4000]

train_x = train_pos + train_neg
test_x = test_pos + test_neg


train_y = np.append(np.ones(len(train_pos)), np.zeros(len(train_neg)))
test_y = np.append(np.ones(len(test_pos)), np.zeros(len(test_neg)))

custom_tweet = "RT @Twitter @chapagain Hello There! Have a great day. :) #good #morning http://chapagain.com.np"


print(process_tweet(custom_tweet))

def count_tweets(result, tweets, ys):
   
    for y, tweet in zip(ys, tweets):
        for word in process_tweet(tweet):

            pair = (word, y)
            
           
            if pair in result:
                result[pair] += 1

            
            else:
                result[pair] = 1

    return result




result = {}
tweets = ['i am happy', 'i am tricked', 'i am sad', 'i am tired', 'i am tired']
ys = [1, 0, 0, 0, 0]
count_tweets(result, tweets, ys)


freqs = count_tweets({}, train_x, train_y)


def train_naive_bayes(freqs, train_x, train_y):
    
    loglikelihood = {}
    logprior = 0

  
    vocab = set([pair[0] for pair in freqs.keys()])
    V = len(vocab)    

    
    N_pos = N_neg = 0
    for pair in freqs.keys():
        if pair[1] > 0:
            N_pos += freqs[pair]
        else:
            N_neg += freqs[pair]
    
    
    D = len(train_y)

    
    D_pos = np.sum(train_y)

    
    D_neg = D - D_pos

    
    logprior = np.log(D_pos) - np.log(D_neg)
    
    
    for word in vocab:
        
        freq_pos = freqs.get((word, 1), 0)
        freq_neg = freqs.get((word, 0), 0)

        
        p_w_pos = (freq_pos + 1) / (N_pos + V)  
        p_w_neg = (freq_neg + 1) / (N_neg + V)  

        
        loglikelihood[word] = np.log(p_w_pos / p_w_neg)

    return logprior, loglikelihood



logprior, loglikelihood = train_naive_bayes(freqs, train_x, train_y)
print(logprior)
print(len(loglikelihood))



def naive_bayes_predict(tweet, logprior, loglikelihood):
   
    
    word_l = process_tweet(tweet)

    
    p = 0

    
    p += logprior

    for word in word_l:
        
        if word in loglikelihood:
            
            p += loglikelihood[word]

    return p



my_tweet = 'She smiled.'
p = naive_bayes_predict(my_tweet, logprior, loglikelihood)
print('The expected output is', p)


my_tweet = 'He laughed.'
p = naive_bayes_predict(my_tweet, logprior, loglikelihood)
print('The expected output is', p)




def test_naive_bayes(test_x, test_y, logprior, loglikelihood, naive_bayes_predict=naive_bayes_predict):
    
    accuracy = 0

    
    y_hats = []
    for tweet in test_x:
        
        if naive_bayes_predict(tweet, logprior, loglikelihood) > 0:
           
            y_hat_i = 1
        else:
           
            y_hat_i = 0

       
        y_hats.append(y_hat_i)

    
    error = np.mean(np.abs(y_hats - test_y))

   
    accuracy = 1 - error

    

    return accuracy


print("Naive Bayes accuracy = %0.4f" %
      (test_naive_bayes(test_x, test_y, logprior, loglikelihood)))



for tweet in ['I am happy', 'I am bad', 'this movie should have been great.', 'great', 'great great', 'great great great', 'great great great great']:
   
    p = naive_bayes_predict(tweet, logprior, loglikelihood)

    print(f'{tweet} -> {p:.2f}')



my_tweet = 'you are bad :('
naive_bayes_predict(my_tweet, logprior, loglikelihood)



def get_ratio(freqs, word):
    
    pos_neg_ratio = {'positive': 0, 'negative': 0, 'ratio': 0.0}
    
    
    pos_words = lookup(freqs, word, 1)
    
    
    neg_words = lookup(freqs, word, 0)
    
    
    pos_neg_ratio['ratio'] = (pos_words + 1) / (neg_words + 1)
    pos_neg_ratio['positive'] = pos_words
    pos_neg_ratio['negative'] = neg_words
   
    
    return pos_neg_ratio


get_ratio(freqs, 'happi')




def get_words_by_threshold(freqs, label, threshold, get_ratio=get_ratio):
    
    word_list = {}

    
    for word, _ in freqs.keys():
        
        pos_neg_ratio = get_ratio(freqs, word)
        
        
        if label == 1 and pos_neg_ratio['ratio'] >= threshold:
            
            word_list[word] = pos_neg_ratio

       
        elif label == 0 and pos_neg_ratio['ratio'] <= threshold:
            
            word_list[word] = pos_neg_ratio

        
    return word_list



get_words_by_threshold(freqs, label=0, threshold=0.05)




get_words_by_threshold(freqs, label=1, threshold=10)



print('Truth Predicted Tweet')
for x, y in zip(test_x, test_y):
    y_hat = naive_bayes_predict(x, logprior, loglikelihood)
    if y != (np.sign(y_hat) > 0):
        print('%d\t%0.2f\t%s' % (y, np.sign(y_hat) > 0, ' '.join(
            process_tweet(x)).encode('ascii', 'ignore')))



# test de fichier de de formulaire 

my_tweet = 'I am  not happy because  I am learning  nlp  and i dont care about learning :)'

p = naive_bayes_predict(my_tweet, logprior, loglikelihood)
print(p)
print("heho")



