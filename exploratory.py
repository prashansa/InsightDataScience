#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:51:45 2020

@author: gupta
"""



import os

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


import bz2
import json

import glob 
import datetime



# filename = '/Users/gupta/Documents/insightprogram/TwitterData/twitter_stream_2019_07_01/03/37.json.bz2'


dirName = '/Users/gupta/Documents/insightprogram/TwitterData/twitter_stream_2019_07_01/'





# keyword = 'ice cream'
keyword = 'cake'

#counter that counts the number of tweets in english, with geo or user location and tweet text, with keyword
count = 0
#goes to 1089, takes 25 minutes to run for this for one day 

                

for hashtag in tweet['entities']['hashtags']:
        text = hashtag['text']
        hashes.append(text)  
        print(tweet['text'])



     
    # for tokens in cleanTweets['tokens']:
    #     for s in tokens:
    #         print(s)
    #         s = re.sub(r'[^\x20-\x7e]', '', s)
    #         # s = re.sub(r'[^ -~].*',r'', s )
    #         # s = re.sub(r'[^\x00-\x7f]',r'', s) 
    #         print(s)
            
            
            
            

for dirs, subdirs, files in os.walk(dirName):

    # for nameofsubdir in subdirs:
    #     print(nameofsubdir)
    for nameoffile in files:
        filename = os.path.join(dirs,nameoffile) 
        # print(filename)
    
        with bz2.BZ2File(filename, 'r') as f:
            for i, line in enumerate(f):
                #each tweet is one line or each tweet is one increment in 'i'
                # if i==2:
                    # break;
                tweet = json.loads(line)
                # print (tweet.keys())
                if "text" in tweet:
                    if "lang" in tweet:
                        # print(tweet['lang'])
                        if tweet['lang']=='en':
                            if "geo" in tweet:    
                                # print (tweet['text'])
                                # print(tweet['geo'])
                                # print(tweet['user']['location'])
                                # print ("-------------------------------------------")
                                
                                if keyword in tweet['text']:
                                    print(tweet['text'])
                                    count = count + 1
                            elif "location" in tweet['user']:
                                # print(tweet['text'])
                                # print(tweet['user']['location'])
                                # print ("-------------------------------------------")
                                # count = count + 1
                                if keyword in tweet['text']:
                                    print(tweet['text'])
                                    count = count + 1
                
    print("total count of tweets with english text with tagged location and keyword=", count)
        
    
    
    
    
        # for key in tweet.keys():
        #     print(key)
        
        # if "created_at" in tweet:
        #     print(tweet['created_at'])
        
        # if "geo" in tweet:
        #     if tweet['geo']!=None:
        #         print(tweet['user']['location'])
        #         print(tweet['user']['screen_name'])
        #         print(tweet['id'])
        #         print(tweet['geo'])
        #         print(tweet['text'])
        #         print(tweet['lang'])
        #         print ("-------------------------------------------")
        # print(json.dumps(tweet, indent=5, sort_keys=True))
        
        

# # def match_loc(tweet):
#         location = 'N/A'
#         locs = tweet['user']['location'].split(',')
#         if len(locs) == 2:
#             loc1 = locs[0].strip().lower().capitalize()
#             loc2 = locs[1].strip().upper()
#             if loc2 in d.values():
#                 location = loc2
#             elif loc2 == 'USA' and loc1 in d:
#                 location = d[loc1]
#     print( [tweet['created_at'], tweet['user']['id'], location,
#             re.findall('#\w+', tweet['text']) + re.findall('@\w+', tweet['text'])])




# with bz2.open(filename, 'r') as bzinput:

#     # txt = bz2.decompress(bzinput)
        
#     # txt =  bz2.decompress(bzinput)
#     tweet_errors = 0
#     current_line = 1
#     # num_lines = len(txt.split('\n'))
#     # for line in txt.split('\n'):  # Loop over the lines in the resulting text file.
#     # for line in iter(lambda : bzinput.read(100 * 1024), b''):  
#     for line in bzinput.read():
#         if current_line % 100 == 0:
#             print('Working on line ' + str(current_line) + '/' + str(num_lines))
#             try:
#                 tweet = json.loads(line)
#             except ValueError:
#                 error_log = {'Date_time': datetime.datetime.now(),
#                             'File_TAR': filename,
#                             'File_BZ2': filename,
#                             'Line_number': current_line,
#                             'Line': line,
#                             }
#                 tweet_errors += 1
#                 # db['error_log'].upsert(error_log, ['File_TAR', 'File_BZ2', 'Line_number'])
#                 print('Error occured, now at ' + str(tweet_errors))
#             try:
#                 tweet_id = tweet['id']
#                 tweet_text = tweet['text']
#                 tweet_locale = tweet['lang']
#                 created_at = tweet['created_at']
#                 tweet_json = tweet
#                 data = {'tweet_id': tweet_id,
#                         'tweet_text': tweet_text,
#                         'tweet_locale': tweet_locale,
#                         'created_at_str': created_at,
#                         'date_loaded': datetime.datetime.now(),
#                         'tweet_json': tweet_json}
#                 # db['tweets'].upsert(data, ['tweet_id'])
#             except KeyError:
#                 error_log = {'Date_time': datetime.datetime.now(),
#                             'File_TAR': filename,
#                             'File_BZ2': bz2_filename,
#                             'Line_number': current_line,
#                             'Line': line,
#                             }
#                 tweet_errors += 1
#                 # db['error_log'].upsert(error_log, ['File_TAR', 'File_BZ2', 'Line_number'])
#                 print('Error occured, now at ' + str(tweet_errors))
#                 continue
    


#
#with bz2.BZ2File(filename, "rt") as bzinput:
#    lines = []
#    for i, line in enumerate(bzinput):
##        if i == 10: break
#        tweets = json.loads(line)
#        lines.append(tweets)
##        print json.dumps(tweets) #, indent=4, sort_keys=True))
##        print i
#        poster=tweets['user']['screen_name']
#        tweet_date=tweets['created_at']
#        tweet_id=tweets['id']
#        tweet_text=tweets['text']
#        print poster, tweet_date, tweet_id, tweet_text
#



