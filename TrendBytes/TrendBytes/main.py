#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:07:49 2020

@author: gupta
"""





searchword = 'cake'

# readJsonFiles(searchword)

csvFile = '/Users/gupta/Documents/insightprogram/outputs/fileWithTweets_2019_07_01_' + searchword + '.csv' 


dfAllTweets = pd.read_csv(csvFile)
dfAllTweets = standardizeText(dfAllTweets, "text")


for i, text in enumerate(dfAllTweets["text"]):
    # print(text)
    itemList = []
    for item in text.split():
        if item[0]!='x':
            if item!='b':
            # print(item)
                itemList.append(item)
    newtext = " ".join(itemList)
    dfAllTweets.at[i, 'text'] = newtext
    


dfAllTweets.drop_duplicates(subset="id", inplace=True)



# # kkk = " ".join(filter(lambda x:x[0]!='x', text.split()))
# kkk = lambda y: " ".join([item for item in y.split() if y[0]!='x' ])
# dfAllTweets["text"] =  dfAllTweets["text"].apply(kkk)


# # #adding the tokens field in the dataframe
dfAllTweets = tokenizerFunction(dfAllTweets, "text")

    
    
dfAllTweets.to_csv('/Users/gupta/Documents/insightprogram/outputs/fileWithTweets_2019_07_01_' + searchword + '_clean.csv')



sid = SentimentIntensityAnalyzer()

polarityscore_negative = []
tweettext_negative = []


polarityscore_positive = []
tweettext_positive = []

polarityscore_neutral  = []
tweettext_neutral = []


for tweettext in dfAllTweets["text"]:
    
    score = sid.polarity_scores(tweettext)
    if score['compound']> 0.0:
        polarityscore_positive.append(score)
        tweettext_positive.append(tweettext)
        
    elif score['compound']==0.0:
        polarityscore_neutral.append(score)
        tweettext_neutral.append(tweettext)
        
    elif score['compound']<0.0:
        polarityscore_negative.append(score)
        tweettext_negative.append(tweettext)
    
    


positive_texty = " ".join(tweettext_positive)
neutral_texty = " ".join(tweettext_neutral)
negative_texty = " ".join(tweettext_negative)


bigList = [positive_texty, neutral_texty, negative_texty]    
    
for g, given in enumerate(bigList):
    
    print (g)
    # # dfAllTweets = pd.read_csv("/Users/gupta/Documents/insightprogram/outputs/fileWithTweets_2019_07_01_cake_clean.csv")
    
    # # # #all words list without the stop words and hex characters starting with x
    # wordList = allWords(dfAllTweets)
    
    wordList = allWords(given)
    
    wordList = [i for i in wordList if not i.isdigit()]
    
    
    # # # vocab = sorted(list(set(wordList)))
    lemWordList = lemmFunction(wordList) 
    
    
    # tagged = nltk.pos_tag(lemWordList)
    # tag_fd = nltk.FreqDist(tag for (word, tag) in tagged)
    # print(tag_fd.most_common())
    
    # print([a[0] for (a, _) in tag_fd.most_common() if a[1] == 'NN'])
    
    
    
    # # # # #finding the most frequently ocurring words
    topWords = mostFrequent(lemWordList)
    # # # 
    
    
    
    #remove single letters again
    lemWordList = [i for i in lemWordList if len(i) > 1]
    
    
    
    
    lemWordList = [x for x in lemWordList if x not in ['actual', 'amp','almost','bitch', 'could','cake', 'complete', 'drop', 'day'
                                                       'eat','effortlessly','feel', 'first', 'friend', 'get','go', 'give', 'horny'
                                                       'know',
                                                       'let', 'like','make', 'man', 'much',
                                                       'nct', 'new','never','need', 'ni', 'nobody',
                                                       'one', 'onstage', 'please', 'pussy', 'really'
                                                       'say','si', 'show','somi', 'serve', 'see',
                                                       'take','tell', 'tf', 'thing', 'try','top', 'today', 'time'
                                                        'year', 'would','woman','want'
                                                        
                                                        ]]
    
    with open('bad-words.txt', 'r') as curseWords:
        lemWordList = [x for x in lemWordList if x not in curseWords]
        
    
    with open('file'+str(g)+".txt", 'w') as f:
        for item in lemWordList:
            f.write("%s\n" % item)
       
    
    
    
    
    
    
    

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
        
    




















