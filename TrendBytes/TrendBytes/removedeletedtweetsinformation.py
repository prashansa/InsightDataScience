#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:22:44 2020

@author: gupta
"""


#file to remove 'deleted tweets' information in the json files, and 
# choose only english tweets to upload to amazon s3 bucket





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




dirName = '/Users/gupta/Documents/insightprogram/TwitterData/twitter_stream_2019_07_01/'

json_files = [pos_json for pos_json in os.listdir(dirName) if pos_json.endswith('.json')]


# print(json_files)

if 0:
    for i, file in enumerate(json_files):
        if i==2:
            with open(os.path.join(dirName, file), 'r') as f:
                for j, line in enumerate(f):
                    if line=='\n':
                        del line
                    else:
                        tweet = json.loads(line)
                        print(tweet)







if 1:
    
    json_lines = []
    
    for i, file in enumerate(json_files):
        # if i==2:
        if i>2:
            with open(os.path.join(dirName, file), 'r') as f:
                # for j, line in enumerate(f):
                for line in f.readlines():
                    tweet = json.loads(line)
                    if "created_at" in tweet:
                        if "lang" in tweet: 
                            if tweet['lang']=='en':
                                json_lines.append(line)
            
                
            with open(os.path.join(dirName, file), 'w') as f2:
                f2.writelines(json_lines)




























