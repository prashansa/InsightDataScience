#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:11:48 2020

@author: gupta
"""

import os 
import pdb


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


import bz2
import json
import csv


import glob 
import datetime
from datetime import datetime
from datetime import timedelta
# from itertools import islice, izip



import collections
from collections import Counter


import nltk 
# nltk.download()
from nltk import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.collocations import *

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical



import sqlite3

import keras
import re
# import codecs


#counter that counts the number of tweets in english, with geo or user location and tweet text, with keyword
    






def bz2tojson(dirName, keyword):
    count = 0
    
    items = []
    
    for dirs, subdirs, files in os.walk(dirName):
        
        for nameoffile in files:
            filename = os.path.join(dirs,nameoffile) 
        
            with bz2.BZ2File(filename, 'r') as f:
                for i, line in enumerate(f):
                    
                    tweet = json.loads(line)
                    
                
                    if "text" in tweet: #the ones with text in them
                        if "lang" in tweet: 
                            # print(tweet['lang'])
                            if tweet['lang']=='en':#the ones that are in english only
                                if keyword in tweet['text']:
                                    if "geo" in tweet: 
                                        if tweet['geo'] is not None: #the ones that have location marked
                                            items.append(tweet)
                                            count = count + 1
                                            print('count of tweets appended=',count)
                                            
                                #or a screen location - may or may not be correct- so i removed it!        
                                # elif "location" in tweet['user']: 
                                #     if tweet['location'] is not None:
                                #         items.append(tweet)
                                #         count = count + 1
                                #         print('count of tweets appended=',count)
                # if count>10:
                    # break;
                    
        # print("total count of tweets with english text with tagged location and keyword=", count)
    return items        
    

def getCSVoutput(aList):
    output = [('geo', 'screenlocation', 'text', 'hashtags')]
    
    # pdb.set_trace()
    
    for item in aList:
        
        if 'text' in item['entities']['hashtags']:
        
            output.append((
                    item['geo'],
                    item['user']['location'],
                    item['text'].encode('utf-8'),
                    item['entities']['hashtags']['text'].encode('utf-8'),
                        ))
        else:
            output.append((
                    item['geo'],
                    item['user']['location'],
                    item['text'].encode('utf-8'),
                    'None',
                        ))
            

    return output 



def writeCSV(aList, csvFile):
    with open(csvFile, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(aList)




def getGeo(d):
    output = [('date', 'tweet', 'lat', 'long')]
    for item in d:
        try:
            lat = item['geo']['coordinates'][0]
            long = item['geo']['coordinates'][1]
            date = item['created_at']
            text = item['text'].encode('utf-8')
            output.append((date, text, lat, long))
       
    return output





def standardize_text(df, text_field):
    
    # pdb.set_trace()
    
    # df[text_field] = df[text_field].str.replace(r'[^\x20-\x7e]', "") #re.sub(r'[^\x20-\x7e]', '', df[text_field])
    df[text_field] = df[text_field].str.replace(r"http\S+", "")
    df[text_field] = df[text_field].str.replace(r"http", "")
    df[text_field] = df[text_field].str.replace(r"@\S+", "")
    df[text_field] = df[text_field].str.replace(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " ")
    df[text_field] = df[text_field].str.replace(r"@", "at")
    df[text_field] = df[text_field].str.lower()
    return df




dirName = ['/Users/gupta/Documents/insightprogram/TwitterData/twitter_stream_2019_07_07/']
           # '/Users/gupta/Documents/insightprogram/TwitterData/twitter_stream_2018_07_17']
           
csvFile = 'fileWithTweets_2019_07_07.csv'


# keyword = 'ice cream'
keyword = ['cake'] #, 'ice cream']




# for d in dirName:
#     for k in keyword:
#         tweetList = bz2tojson(d,k)
    
#         tweetCSVoutput = getCSVoutput(tweetList)
    

#         writeCSV(tweetCSVoutput, csvFile)


if 1: 
    
    # dfAllTweets = pd.read_csv(csvFile)
    
    # dfAllTweets = standardize_text(dfAllTweets, "text")
    
    # dfAllTweets.to_csv("fileWithTweets_2019_07_07_clean.csv")
    
    
    ##########  TOKENIZATION and STOP WORDS
    tokenizer = RegexpTokenizer(r'\w+')
    stop = set(stopwords.words('english')) 
    
    cleanTweets= pd.read_csv('fileWithTweets_2019_07_01_clean.csv')
    cleanTweets["tokens"] = cleanTweets["text"].apply(tokenizer.tokenize)
    
    #this is not working in pandas dataframe directly, i will remove stop words in the vocab list below 
    # cleanTweets["cleanTokens"] = [wo for tok in cleanTweets["tokens"] for wo in tok  if (not wo in stop)]
               
    # cleanTweets.to_csv("fileWithTweets_2019_07_07_clean_tokens.csv")
   
            
    all_words = [word for tokens in cleanTweets["tokens"] for word in tokens if not word in stop]
    all_words = [word for word in all_words if not word.startswith('x')]
    
    
    
    sentence_lengths = [len(tokens) for tokens in cleanTweets["tokens"]]
    VOCAB = sorted(list(set(all_words)))
    
    print("%s words total, with a vocabulary size of %s" % (len(all_words), len(VOCAB)))
    print("Max sentence length is %s" % max(sentence_lengths))
    
        
        
    # writeCSV(all_words, 'fileWithTweets_2019_07_07_all_words.csv')
    
    
    # use nltk fdist to get a frequency distribution of all words
    fdist = FreqDist(all_words)
    print(len(fdist)) # number of unique words
    
    fdist.plot()
    
    
    
#     # fig = plt.figure(figsize=(10, 10)) 
#     # plt.xlabel('Sentence length')
#     # plt.ylabel('Number of sentences')
#     # plt.title("%s words total, with a vocabulary size of %s" % (len(all_words), len(VOCAB)))
#     # plt.hist(sentence_lengths)
#     # # # plt.show()
    
#     # plt.savefig('histogramOfSentenceLengths.png')
    
    
    # writeCSV(collections.Counter(all_words).most_common(), 'fileWithTweets_2019_07_07_mostCommonWords.csv')
    # print(collections.Counter('cake'))
    
    
    lem = WordNetLemmatizer()
    # # tokenized = nltk.word_tokenize(text)
    
    listOfLemVocab= []
    for aword in VOCAB:
        lemmatizedVOCAB = lem.lemmatize(aword, pos="v")
        # print(lemmatizedVOCAB)
        listOfLemVocab.append(str(lemmatizedVOCAB))
            
    # writeCSV(listOfLemVocab, 'fileWithTweets_2019_07_07_lemmatizedVocab.csv')    
        # writer.writerows(lemmatizedVOCAB)
    



    bigram_measures = nltk.collocations.BigramAssocMeasures()
    trigram_measures = nltk.collocations.TrigramAssocMeasures()
    
    
    finder = BigramCollocationFinder.from_words(all_words)
    
    scored = finder.score_ngrams(bigram_measures.raw_freq)

    k = sorted(finder.nbest(bigram_measures.raw_freq, 500))
    writeCSV(k, 'afile-01.csv')
    
    
    

############### COLLOCATIONS USING FINDERS ###################

if 0:
    
    file1 = pd.read_csv('fileWithTweets_2019_07_01_clean_tokens.csv')
    file2 = pd.read_csv('fileWithTweets_2019_07_02_clean_tokens.csv')
    file3 = pd.read_csv('fileWithTweets_2019_07_03_clean_tokens.csv')
    file4 = pd.read_csv('fileWithTweets_2019_07_04_clean_tokens.csv')
    file5 = pd.read_csv('fileWithTweets_2019_07_05_clean_tokens.csv')
    file6 = pd.read_csv('fileWithTweets_2019_07_06_clean_tokens.csv')
    file7 = pd.read_csv('fileWithTweets_2019_07_07_clean_tokens.csv')
    
    
    stop = set(stopwords.words('english')) 
    
    
    words1 = [word for tokens in file1["tokens"] for word in tokens if not word in stop]
    words1 = [word for word in words1 if not word.startswith('x')]
    
    words2 = [word for tokens in file2["tokens"] for word in tokens if not word in stop]
    words2 = [word for word in words2 if not word.startswith('x')]
    
    words3 = [word for tokens in file3["tokens"] for word in tokens if not word in stop]
    words3 = [word for word in words3 if not word.startswith('x')]
    
    words4 = [word for tokens in file4["tokens"] for word in tokens if not word in stop]
    words4 = [word for word in words4 if not word.startswith('x')]
    
    words5 = [word for tokens in file5["tokens"] for word in tokens if not word in stop]
    words5 = [word for word in words5 if not word.startswith('x')]
    
    words6 = [word for tokens in file6["tokens"] for word in tokens if not word in stop]
    words6 = [word for word in words6 if not word.startswith('x')]
    
    words7 = [word for tokens in file7["tokens"] for word in tokens if not word in stop]
    words7 = [word for word in words7 if not word.startswith('x')]
    
    
    # all_words.append()
    
    
    
    
    
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    trigram_measures = nltk.collocations.TrigramAssocMeasures()
    
    
    finder = BigramCollocationFinder.from_words(words1)
    
    scored = finder.score_ngrams(bigram_measures.raw_freq)

    k = sorted(finder.nbest(bigram_measures.raw_freq, 500))
    
    


    




if 0: 
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    trigram_measures = nltk.collocations.TrigramAssocMeasures()
    
    
    text = "I do not like green eggs and ham, I do not like them Sam I am!"
    tokens = nltk.wordpunct_tokenize(text)
    finder = BigramCollocationFinder.from_words(tokens)
    scored = finder.score_ngrams(bigram_measures.raw_freq)
    print(sorted(bigram for bigram, score in scored))
    
    
    
    # construct the collocation finder from manually-derived FreqDists:
    word_fd = nltk.FreqDist(tokens)
    bigram_fd = nltk.FreqDist(nltk.bigrams(tokens))
    finder = BigramCollocationFinder(word_fd, bigram_fd)
    print(scored == finder.score_ngrams(bigram_measures.raw_freq))
    
    
    # for trigrams:
    finder = TrigramCollocationFinder.from_words(tokens)
    scored = finder.score_ngrams(trigram_measures.raw_freq)
    print(set(trigram for trigram, score in scored) == set(nltk.trigrams(tokens)))
    
    
    #want to select only the top n results:
    print(sorted(finder.nbest(trigram_measures.raw_freq, 3)))
    
    # Alternatively, we can select those above a minimum score value:
    print(sorted(finder.above_score(trigram_measures.raw_freq,
                              1.0 / len(tuple(nltk.trigrams(tokens))))))
    
    #Now spanning intervening words:
    finder = TrigramCollocationFinder.from_words(tokens)
    finder = TrigramCollocationFinder.from_words(tokens, window_size=4)
    print(sorted(finder.nbest(trigram_measures.raw_freq, 4)))
    
    
    #closer look at the finder's ngram frequencies:
    print(sorted(finder.ngram_fd.items(), key=lambda t: (-t[1], t[0]))[:10])
    
























# if __name__ == "__main__":
#     main()














































