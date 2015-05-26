# NLP_Project
GWU NLP Class 2015
Project Members - Josh Winters, Mikhail Flom, Derrick Stucky and John Yoo

POV Character Sentiment Analysis in ASOIF 

These files can be used to perform sentiment analysis in Python 2.7, using textblob and the PatternAnalyzer, 
on each of the characters in the A Song of Ice & Fire ASOIF) series of novels, also known as the HBO Series Game of Thrones

Generally what we are trying to do is look perform sentiment analysis on units of text, either sentences or paragraphs, 
for each POV character, whenver one of the major Houses of GoT are mentioned.  

For example, in Chapter One of the first book, A Game of Thrones, we scanned all paragraphs for the presence of the word "Lannister"
And whenever "Lannister" was obseved in a paragraph, we used the textblob function sentiment to perform sentiment analysis on that 
paragraph.  Thereby attempting to understand the view of the House Lannister, from the point of view of the character Arya.  

And so we did this for all POV characters, in all books, and were able to visualize the total sentiment as well as the change in 
sentiment for each of the Houses, for all of the books, and from each characters POV. 

To replicate the data please start by downloading the source data, which is 30 text files that can be found in the TextFiles.zip folder.  Please sett your working directory to whatever folder you have stored the txt files in.

Then you can begin the sentiment analysis by running the two sentiment analyzer python files first and then opening up the 
All_Character_Sentiment.py file and following the instructions within the file.

Following these instructions should yield 8 xlsx files which have the sentiment polarity observations for each character for each book.
The reason there are 8 is that we have performed the analysis twice for each character, once with sentences as the base unit of text 
and the other with paragraphs as the base unit of text, the output files are labeled accordingly.

If you would like to see the raw results in the excel file format, there is a folder called Sent_Results which has the polarity for each obsevation, for each character, for each book and for sentences and paragraphs.

The python files All_Character_Sentiment.py, sent_analyzer_para.py and sent_analyzer_sent were written by Josh Winters.
