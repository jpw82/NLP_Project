# -*- coding: utf-8 -*-
"""
Created on Fri May 22 15:21:30 2015

@author: Josh New
"""

import textblob as tb
import pandas as pd

def sentiment_analyzer_sent(txt_file,targets):

    #returns a list of data frames. the first dataframe is the polarity of each unit of text which was
    #identifed as containing the target.  The second dataframe is the subjectivity of that unit of text 
    with open(txt_file,"r") as textfile:
        content = textfile.read()
    
    content = tb.TextBlob(content).sentences
     
    target_dict = {key: list() for key in targets}
                  
    for i in targets:
        for c in content:        
            if i in c:
                target_dict[i].append(c)
                
    target_sent_pol_dict = {key: list() for key in targets} 
    
    target_sent_sub_dict = {key: list() for key in targets}  
                  
    for h in target_dict:
        for i in target_dict[h]:
            target_sent_pol_dict[h].append(i.sentiment.polarity)
        for s in target_dict[h]:
            target_sent_sub_dict[h].append(s.sentiment.subjectivity)
            
    final_sent_pol_dict = {key: list() for key in targets} 
    
    final_sent_sub_dict = {key: list() for key in targets} 
                  
    for p in target_dict:
        x = pd.Series(target_sent_pol_dict[p])
        y = pd.Series(target_sent_sub_dict[p])        
        final_sent_pol_dict[p] = x
        final_sent_sub_dict[p] = y
        
    pol_df = pd.DataFrame.from_dict(final_sent_pol_dict)
    sub_df = pd.DataFrame.from_dict(final_sent_sub_dict)
    
    df_list = [pol_df,sub_df]
    
    return df_list
        
        