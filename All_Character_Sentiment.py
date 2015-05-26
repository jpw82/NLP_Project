# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:37:03 2015

@author: Josh New
"""

import textblob as tb
import pandas as pd
import os


###To start the sentiment analysis please first run the provided files: sent_analyzer_para.py and
### the file sent_analyzer_sent.py 

### Then to get started on performing the sentiment analysis on the characters in each book 
## PLEASE RUN FIRST THE CODE BETWEEN HERE
books = ["One","Two","Three","Four"]

pov_characters = ["Areo","Arya","Asha","Bran","Cersei","Catelyn","Daenerys","Davos",
"Eddard","Jaimie","Jon","Sansa","Samwell","Theon","Tyrion","Victarion"]
             
houses = ["Stark","Lannister","Baratheon","Targaryen","Tully",
"Martell","Greyjoy","Arryn","Tyrell","Frey","Bolton","Baelish"]


###get the current working directory
workingdir = os.getcwd()

#list all the file sin the current working directory

files = os.listdir(workingdir)

##now make a list of files in the working directory

filepaths = []

for f in files:
    foo = workingdir + "\\" + f    
    filepaths.append(foo)

#### AND HERE, FIRST


###ONCE YOU HAVE RUN THE ABOVE CODE YOU CAN RUN THE REST IN ONE SHOT

##this code will perform sentiment analysis on each of the text files in the working directory, which are
##character books and then spits out an excel file for each book, and each sentiment type, which has 
##all sentiment polarity observations for each character towards each house, where each character has a 
##seperate excel tab.

##To get started:
##Make some containers for sentiment analysis, book # is the main key, then within that key is a another dictionary 
## where the characters are keys and an empty list is the value.  this is where we will put the sentiment observations
    

book_dict_paragraphs = {"One":{key: list() for key in pov_characters},"Two":{key: list() for key in pov_characters},
"Three":{key: list() for key in pov_characters},"Four":{key: list() for key in pov_characters}}

book_dict_sentences = {"One":{key: list() for key in pov_characters},"Two":{key: list() for key in pov_characters},
"Three":{key: list() for key in pov_characters},"Four":{key: list() for key in pov_characters}}



##note that each time the sentiment analyzers are run they return a list of data frames with the 
##first DF being the sentiment, using the PatternAnalyzer, for each observation, whether that be 
##sentences of paragraphs, and the second data frame is the subjectitivity of that observation. 

##Note that all of the files that sentiment analysis are being perfromed must be in the working directory
##and the working directory must be set for the sentiment analyzer files as well.

for b in books:
    for f in filepaths:
        if b in f:
            print "Performing Sentiment Analysis on Book", b
            for p in pov_characters:
                if p in f:
                    print "And on character", p                    
                    #sentiment analysis on character p for book b                    
                    sent_para = sentiment_analyzer_para(f,houses)
                    book_dict_paragraphs[b][p].append(sent_para)
                    sent_sent = sentiment_analyzer_sent(f,houses)
                    book_dict_sentences[b][p].append(sent_para)
                    
                else:
                    continue
        else:
            continue

####Now I want to take only the polarity readings for each book/character and put it into a pandas panel
###for export to an excel spreadsheet where each tab is the polarity observations for each character towards
###each house.  Do this for each book and then for each text unit, sentence and paragraphs.  

keys = pov_characters

###BOOK ONE
## make an empty dictionary to store each characters polarity data frame, where key is the characters name and 
## the value is None

book_one_panel_dict_para = {key: None for key in keys}
book_one_panel_dict_sentences = {key: None for key in keys}

for p in pov_characters:
    a = book_dict_paragraphs["One"][p]
    b = book_dict_sentences["One"][p]
    if len(a) != 0:
        
        ##remeber that a is a single item list, which contains a list with two items (pol and subj data frames)
        ##and so to retrieve the first item of the second list(pol data frame), we do it like this
        
        book_one_panel_dict_para[p] = a[0][0]
        
    else:
        continue
    if len(b) != 0:
        book_one_panel_dict_sentences[p] = b[0][0]
    else:
        continue

###its easy to make a pandas panel from a dictionary of data frames and so     
book_one_panel_para = pd.Panel(book_one_panel_dict_para)
book_one_panel_sentences = pd.Panel(book_one_panel_dict_sentences)

book_one_panel_para.to_excel("book_one_para.xlsx")
book_one_panel_sentences.to_excel("book_one_senteces.xlsx")

####BOOK TWO

book_two_panel_dict_para = {key: None for key in keys}
book_two_panel_dict_sentences = {key: None for key in keys}

for p in pov_characters:
    a = book_dict_paragraphs["Two"][p]
    b = book_dict_sentences["Two"][p]
    if len(a) != 0:
        book_two_panel_dict_para[p] = a[0][0]
    else:
        continue
    if len(b) != 0:
        book_two_panel_dict_sentences[p] = b[0][0]
    else:
        continue
    
book_two_panel_para = pd.Panel(book_two_panel_dict_para)
book_two_panel_sentences = pd.Panel(book_two_panel_dict_sentences)

book_two_panel_para.to_excel("book_two_para.xlsx")
book_two_panel_sentences.to_excel("book_two_senteces.xlsx")

######BOOK THREE

book_three_panel_dict_para = {key: None for key in keys}
book_three_panel_dict_sentences = {key: None for key in keys}

for p in pov_characters:
    a = book_dict_paragraphs["Three"][p]
    b = book_dict_sentences["Three"][p]
    if len(a) != 0:
        book_three_panel_dict_para[p] = a[0][0]
    else:
        continue
    if len(b) != 0:
        book_three_panel_dict_sentences[p] = b[0][0]
    else:
        continue
    
book_three_panel_para = pd.Panel(book_three_panel_dict_para)
book_three_panel_sentences = pd.Panel(book_three_panel_dict_sentences)

book_three_panel_para.to_excel("book_three_para.xlsx")
book_three_panel_sentences.to_excel("book_three_senteces.xlsx")

####BOOK FOUR

book_four_panel_dict_para = {key: None for key in keys}
book_four_panel_dict_sentences = {key: None for key in keys}

for p in pov_characters:
    a = book_dict_paragraphs["Four"][p]
    b = book_dict_sentences["Four"][p]
    if len(a) != 0:
        book_four_panel_dict_para[p] = a[0][0]
    else:
        continue
    if len(b) != 0:
        book_four_panel_dict_sentences[p] = b[0][0]
    else:
        continue
    
book_four_panel_para = pd.Panel(book_four_panel_dict_para)
book_four_panel_sentences = pd.Panel(book_four_panel_dict_sentences)

book_four_panel_para.to_excel("book_four_para.xlsx")
book_four_panel_sentences.to_excel("book_four_senteces.xlsx")



