from flask import Flask
from flask import render_template
from flask import request

from TrendBytes import app 


# from myInsightApp import functions_file


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





# Create the application object
#app = Flask(__name__)

app.secret_key = "random"

@app.route('/',methods=["GET","POST"]) #we are now using these methods to get user input
def home_page():
	return render_template('index.html')  # render a template

@app.route('/output')
def trendit_output():
#  	 
# Pull input
    searchword = request.args.get('searchword')  #what you want to know about
    lastdays = request.args.get('lastdays')    #no. of days last 1 day, last 2 days, last 7 days etc  	  
         
      
   	# Case if empty
    if searchword =="":
    	return render_template("index.html", searchword = searchword, my_form_result="Empty")
    elif lastdays=="":
        return render_template("index.html", lastdays = lastdays, my_form_result="Empty")
    else:
        
        # print(searchword)
        
        totalnooftweets = 7554 # readJsonFiles(searchword)
          
        positive_image = "newwordcloud-positive.png"
        
        negative_image = "newwordcloud-negative.png"
      
        return render_template("index.html", searchword= searchword, lastdays=lastdays, totalnooftweets=totalnooftweets, 
                                positive_image=positive_image,negative_image =negative_image,
                                form_result="NotEmpty")













# # start the server with the 'run()' method
#if __name__ == "__main__":
#  	 app.run(debug=True) #will run locally http://127.0.0.1:5000/
