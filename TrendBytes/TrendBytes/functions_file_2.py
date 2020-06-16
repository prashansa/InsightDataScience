#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:07:49 2020

@author: gupta
"""

import os 
from os import path
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
from nltk.corpus import wordnet

from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.collocations import *
from nltk.collocations import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# from keras.preprocessing.text import Tokenizer
# from keras.preprocessing.sequence import pad_sequences
# from keras.utils import to_categorical

import unicodedata
from unidecode import unidecode

import sqlite3

import keras
import re
# import codecs




from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator



import warnings # ignore warnings 
warnings.filterwarnings("ignore")
import seaborn as sns
sns.set(style="white", color_codes=True)





def readJsonFiles(searchword):

    # counter to count the total number of tweets for a given search word
    counter = 0
    
    items = []
    
    dirName = '/Users/gupta/Documents/insightprogram-1/TwitterData/twitter_stream_2019_07_01/'

    json_files = [pos_json for pos_json in os.listdir(dirName) if pos_json.endswith('.json')]

    # pdb.set_trace()

    for i, file in enumerate(json_files):
           with open(os.path.join(dirName, file), 'r') as f:
               for j, line in enumerate(f):
                   if line=='\n':
                       del line
                   else:
                       tweet = json.loads(line)
                       # print(tweet)
                       if "lang" in tweet: 
                           if tweet['lang']=='en':
                               if "text" in tweet:
                                   re.sub(r"@\S+", " ", tweet['text'])
                                   if searchword in tweet['text']:
                                       # print(tweet['text'])
                                       counter = counter + 1
                                       items.append(tweet)
                                       print(counter, 'out of', i, 'files')
    
    
    tweetCSVoutput = getCSVoutput(items)
    
    csvFile = '/Users/gupta/Documents/insightprogram-1/outputs/fileWithTweets_2019_07_01_' + searchword + '.csv' 

    writeCSV(tweetCSVoutput,csvFile)


                          
    return counter




# https://stackoverflow.com/questions/43797500/python-replace-unicode-emojis-with-ascii-characters/43813727#43813727

# def deEmojify(inputString):
#     returnString = ""

#     for character in inputString:
#         try:
#             character.encode("ascii")
#             returnString += character
#         except UnicodeEncodeError:
#             replaced = unidecode(str(character))
#             if replaced != '':
#                 returnString += replaced
#             else:
#                 try:
#                       returnString += "[" + unicodedata.name(character) + "]"
#                 except ValueError:
#                       returnString += "[x]"

#     return returnString



# https://stackoverflow.com/questions/55329741/removing-emojis-that-start-with-x-in-pandas-python-when-reading-a-csv-file

def deEmojify(inputString): 
    returnString = "" 
    for character in inputString: 
        try: 
            character.encode("ascii") 
            returnString += character 
        except UnicodeEncodeError: 
            returnString += '' 
    return returnString 

















def getCSVoutput(aList):
    output = [('id', 'id_str','geo', 'screenlocation', 'text', 'hashtags')]
    
    # pdb.set_trace()
    
    for item in aList:
        
        if 'text' in item['entities']['hashtags']:
        
            output.append((
                    item['id'],
                    item['id_str'],
                    item['geo'],
                    item['user']['location'],
                    item['text'].encode('utf-8'),
                    item['entities']['hashtags']['text'].encode('utf-8'),
                        ))
        else:
            output.append((
                    item['id'],
                    item['id_str'],
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






contraction_patterns = [ (r'won\'t', 'will not'), (r'can\'t', 'cannot'), (r'i\'m', 'i am'), (r'ain\'t', 'is not'), (r'(\w+)\'ll', '\g<1> will'), (r'(\w+)n\'t', '\g<1> not'),
                         (r'(\w+)\'ve', '\g<1> have'), (r'(\w+)\'s', '\g<1> is'), (r'(\w+)\'re', '\g<1> are'), (r'(\w+)\'d', '\g<1> would'), (r'&', 'and'), (r'dammit', 'damn it'), (r'dont', 'do not'), (r'wont', 'will not') ]




def replaceContraction(text):
        patterns = [(re.compile(regex), repl) for (regex, repl) in contraction_patterns]
        for (pattern, repl) in patterns:
            (text, count) = re.subn(pattern, repl, text)
        return text


def standardizeText(df, textField):
    
    # pdb.set_trace()
    

    for text in df[textField]:
        replaceContraction(text)
        # text = re.sub(':\)|;\)|:-\)|\(-:|:-D|=D|:P|xD|X-p|\^\^|:-*|\^\.\^|\^\-\^|\^\_\^|\,-\)|\)-:|:\'\(|:\(|:-\(|:\S|T\.T|\.\_\.|:<|:-\S|:-<|\*\-\*|:O|=O|=\-O|O\.o|XO|O\_O|:-\@|=/|:/|X\-\(|>\.<|>=\(|D:', ' ', text)
        re.sub(r"\b[a-zA-Z]\b", " ", text)
        text = ''.join([i for i in text if not i.isdigit()])   
        deEmojify(text)
        
        # print(text)
        
        
    df[textField] = df[textField].str.replace('b\'RT', " ")
    df[textField] = df[textField].str.replace('b\"RT', " ")
  
    df[textField] = df[textField].str.replace('((www\.[^\s]+)|(https?://[^\s]+))', " ")
    df[textField] = df[textField].str.replace(r"(\\u[0-9A-Fa-f]+)", " ")
    df[textField] = df[textField].str.replace(r"[^\x00-\x7f]", " ") #re.sub(r'[^\x20-\x7e]', '', df[text_field])
    df[textField] = df[textField].str.replace(r"http\S+", " ")
    df[textField] = df[textField].str.replace(r"http", " ")
    df[textField] = df[textField].str.replace(r"@\S+", " ")
    df[textField] = df[textField].str.replace(r"[^A-Za-z0-9(),!?@\'\`\"\_\n]", " ")
    df[textField] = df[textField].str.replace(r"@", " ")
    df[textField] = df[textField].str.replace(r'#([^\s]+)'," ") #hashtags in front of a word
    df[textField] = df[textField].str.replace(r"(\!)\1+"," ") #multi exclamation mark
    df[textField] = df[textField].str.replace(r"(\?)\1+"," ") #repetitions of question marks
    df[textField] = df[textField].str.replace(r"(\.)\1+"," ") #multi stop mark
    df[textField] = df[textField].str.lower()
    


    

    
    return df







def tokenizerFunction(df,textField):
    
    tokenizer = RegexpTokenizer(r'\w+')
    df['tokens'] = df[textField].apply(tokenizer.tokenize)
    
    
    return df





def allWords(string):
    
    #for df
    # stop = set(stopwords.words('english')) 
    # allWords =  [word for tokens in df["tokens"] for word in tokens if not word in stop]
    # allWords = [word for word in allWords if not word.startswith('x')]
    
    
    #for string
    
    stop = set(stopwords.words('english')) 
    word_tokens = word_tokenize(string) 
    allWords = [w for w in word_tokens if not w in stop] 
    allWords = [word for word in allWords if not word.startswith('x')]
    
    
    
    
    return allWords




def mostFrequent(wordList):
    
    bigram_measures = nltk.collocations.BigramAssocMeasures()
  
    finder = BigramCollocationFinder.from_words(wordList)
    
    scored = finder.score_ngrams(bigram_measures.raw_freq)

    k = sorted(finder.nbest(bigram_measures.raw_freq, 5))


    return k







#map NLTK’s POS tags
#Map POS tag to first character lemmatize() accepts    

def getWordnetPos(word):

    tag = nltk.pos_tag([word])[0][1][0].upper() 
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)



def lemmFunction(vocab):


    lem = WordNetLemmatizer()
    # # tokenized = nltk.word_tokenize(text)
    
    listOfLemVocab= []
    for aword in vocab:
        lemmatizedVOCAB = lem.lemmatize(aword, pos=getWordnetPos(aword))
        # print(lemmatizedVOCAB)
        listOfLemVocab.append(str(lemmatizedVOCAB))
            

    return listOfLemVocab












############################################################################################

















# searchword = 'cake'

# # readJsonFiles(searchword)

# csvFile = '/Users/gupta/Documents/insightprogram/outputs/fileWithTweets_2019_07_01_' + searchword + '.csv' 


# dfAllTweets = pd.read_csv(csvFile)
# dfAllTweets = standardizeText(dfAllTweets, "text")


# for i, text in enumerate(dfAllTweets["text"]):
#     # print(text)
#     itemList = []
#     for item in text.split():
#         if item[0]!='x':
#             if item!='b':
#             # print(item)
#                 itemList.append(item)
#     newtext = " ".join(itemList)
#     dfAllTweets.at[i, 'text'] = newtext
    


# dfAllTweets.drop_duplicates(subset="id", inplace=True)



# # # kkk = " ".join(filter(lambda x:x[0]!='x', text.split()))
# # kkk = lambda y: " ".join([item for item in y.split() if y[0]!='x' ])
# # dfAllTweets["text"] =  dfAllTweets["text"].apply(kkk)


# # # #adding the tokens field in the dataframe
# dfAllTweets = tokenizerFunction(dfAllTweets, "text")

    
    
# dfAllTweets.to_csv('/Users/gupta/Documents/insightprogram/outputs/fileWithTweets_2019_07_01_' + searchword + '_clean.csv')



# sid = SentimentIntensityAnalyzer()

# polarityscore_negative = []
# tweettext_negative = []


# polarityscore_positive = []
# tweettext_positive = []

# polarityscore_neutral  = []
# tweettext_neutral = []


# for tweettext in dfAllTweets["text"]:
    
#     score = sid.polarity_scores(tweettext)
#     if score['compound']> 0.0:
#         polarityscore_positive.append(score)
#         tweettext_positive.append(tweettext)
        
#     elif score['compound']==0.0:
#         polarityscore_neutral.append(score)
#         tweettext_neutral.append(tweettext)
        
#     elif score['compound']<0.0:
#         polarityscore_negative.append(score)
#         tweettext_negative.append(tweettext)
    
    


# positive_texty = " ".join(tweettext_positive)
# neutral_texty = " ".join(tweettext_neutral)
# negative_texty = " ".join(tweettext_negative)


# bigList = [positive_texty, neutral_texty, negative_texty]    
    
# for g, given in enumerate(bigList):
    
#     print (g)
#     # # dfAllTweets = pd.read_csv("/Users/gupta/Documents/insightprogram/outputs/fileWithTweets_2019_07_01_cake_clean.csv")
    
#     # # # #all words list without the stop words and hex characters starting with x
#     # wordList = allWords(dfAllTweets)
    
#     wordList = allWords(given)
    
#     wordList = [i for i in wordList if not i.isdigit()]
    
    
#     # # # vocab = sorted(list(set(wordList)))
#     lemWordList = lemmFunction(wordList) 
    
    
#     # tagged = nltk.pos_tag(lemWordList)
#     # tag_fd = nltk.FreqDist(tag for (word, tag) in tagged)
#     # print(tag_fd.most_common())
    
#     # print([a[0] for (a, _) in tag_fd.most_common() if a[1] == 'NN'])
    
    
    
#     # # # # #finding the most frequently ocurring words
#     topWords = mostFrequent(lemWordList)
#     # # # 
    
    
    
#     #remove single letters again
#     lemWordList = [i for i in lemWordList if len(i) > 1]
    
    
    
    
#     lemWordList = [x for x in lemWordList if x not in ['actual', 'amp','almost','bitch', 'could','cake', 'complete', 'drop', 'day'
#                                                        'eat','effortlessly','feel', 'first', 'friend', 'get','go', 'give', 'horny'
#                                                        'know',
#                                                        'let', 'like','make', 'man', 'much',
#                                                        'nct', 'new','never','need', 'ni', 'nobody',
#                                                        'one', 'onstage', 'please', 'pussy', 'really'
#                                                        'say','si', 'show','somi', 'serve', 'see',
#                                                        'take','tell', 'tf', 'thing', 'try','top', 'today', 'time'
#                                                         'year', 'would','woman','want'
                                                        
#                                                         ]]
    
#     with open('bad-words.txt', 'r') as curseWords:
#         lemWordList = [x for x in lemWordList if x not in curseWords]
        
    
#     with open('file'+str(g)+".txt", 'w') as f:
#         for item in lemWordList:
#             f.write("%s\n" % item)
       
    
    
    
    
    
    
    

with open("/Users/gupta/Documents/insightprogram-1/myInsightApp/myInsightApp/file-positive.txt", 'r') as filer:    
    wordslist = [x for x in filer]
    

wordslist = [x for x in wordslist if x not in ["''\n", "n't\n", "cake" ]]
    
    
wordslist = list((map(str.strip, wordslist)))


topWordsToPrint = mostFrequent(wordslist)
    
listOfMostCommonWords = collections.Counter(wordslist).most_common(20)

fdist = FreqDist(wordslist)
 
# fdist = FreqDist(wordslist)
# print(len(fdist)) # number of unique words
    
# # # # texty = dfAllTweets.text[0]

# # texty = " ".join(wordy for wordy in dfAllTweets.text)


wordcloud = WordCloud(collocations=False,max_words=30, max_font_size=40, background_color="black", normalize_plurals =True).generate_from_frequencies(fdist)
# plt.figure(figsize=(20,10))
wordcloud.to_file("testing new wordcloud.png")
# plt.tight_layout(pad=0)
plt.imshow(wordcloud)
plt.axis("off")

# plt.show()
        
    
    



















































