
<p align="center">
<img src="https://github.com/prashansa/InsightDataScience/blob/master/TrendBytes/TrendBytes/static/images/logo-final.png" width="400" height="150">
</p>  





# TrendBytes
An App that promises to add value to your business by leveraging trends on the web. 

### Think.. 
There are a lot of times when you might have wished, that the amazing local bakery shop down the street, magically start selling your favorite strawberry cheesecake. 

If you are that bakery owner, you might have come across times where you felt that people are not buying what you are selling. 

### The Problem
The key to finding buyers is to actually listen to them. In this digital era, especially post covid-19, every person is living their life online. This means that the shop owners have to be online, listening to what the market is saying. 

But, local shop owners may not necessarily be social-media savvy, or may not have the capital or personnel to dedicate on social media R&D on an everyday basis. 

### So where does TrendBytes come in? 
There is a need for a solution that can empower the local shop owners. What if an app can deliver all the insights relevant to the shop business everyday? 

TrendBytes obtains its data from Twitter, asks the owner to input a searchword relevant to their business along with the dates in which they are interested, and then spits out the most loved and the least favorite topics in the form of eye catching wordclouds. 


### How was the app developed? 

<p align="center">
<img src="https://github.com/prashansa/InsightDataScience/blob/master/TrendBytes/TrendBytes/static/images/pipeline_trendBytes.png" width="700" height="400">
</p>  


### How does TrendBytes work? 
For the case of a bakery owner, lets assume a searchword "cake", with date as yesterday. The app gives two wordclouds categorized as favorite and disliked. 

* The happy category can then be used by the owner to understand what people like, and then can consider adding them to their offerings on the menu. 

* The disliked category can be used as a disclaimer, so that the owner understands why sales associated with those products might be low. 




<p float="center">
<img src="https://github.com/prashansa/InsightDataScience/blob/master/TrendBytes/TrendBytes/static/images/newwordcloud-positive.png" width="49%" height="250" title="IN DEMAND" />
<img src="https://github.com/prashansa/InsightDataScience/blob/master/TrendBytes/TrendBytes/static/images/newordcloud-negative.png" width="49%" height="250" title="DISLIKED"/>
</p>  







#### Every day use of this app can help the local shop owner understand the trends of the neighbourhood, country and the global industry as whole. The local trends will help them cater specifically to the local needs, and global trends help them evolve and diversify their menu instead of being the frog in the well. 

#### This app is especially useful when shop owners rely on word of mouth for running their business, they can now inform their business and optimize according to the market. 


### Possible Expansions
For next steps, 

1. Elasticsearch (ELK stack) - does not work in the current status. I tried implementing it for 3 days only. Needs more time. Which is why the json files for tweets are loaded and read sequentially, that makes the entire pipeline really slow. ELK will index each tweet json file, and make the search real - time. This is the next immediate step. 

2. The dataset is only limited to 7 days spritzer version from https://archive.org/details/twitterstream. Once the above step is complete, more data can be stored on AWS, which will give access to more days of data. 

3. Twitter API developer account was recently approved (July 4, 2020). This API will be connected to the pipeline on AWS, so real time data can be input. 

4. Expand to other platforms - Add Instagram and Facebook APIs

5. Add image based search - where the owner can search for "cake image" rather than text, for new design inspirations and checking whether people are liking those designs or not. 

6. Extend to Google News API - so that the owner can input information about themselves and their employees and stay informed on relevant news items. For example, they could be informed about new wage subsidy programs introduced by the Canadian govt during covid-19 pandemic that will be directly relevant to the employees. 

# Insight Data Science

This project was made during the Insight Data Science (Toronto) program, within 4 weeks. 

* Week 1 was brainstorming projects that solve a business problem. 

* Week 2 was about implementing the most basic solution and presenting a Minimal Viable Product. 

* Week 3 involved more focus on adding validation to the machine learning models used and making a live app hosted online, and presenting a Minimal Viable Demo. 

* Week 4 was about polishing that demo and improving the business pitch with recognition of pitfalls and applicability of the product. 









