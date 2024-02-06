# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 13:43:04 2023

@author: jwark
"""

"""
#problem statement:
    
You are parsing a news story from cnbc.com. News story is stores in news_story.txt which is on whatsapp. 
You need to, 
1.	Extract all NOUN tokens from this story. You will have to read the file in python first to 
collect all the text and then extract NOUNs in a python list
2.	Extract all numbers (NUM POS type) in a python list
3.	Print a count of all POS tags in this story
"""
import nltk
from nltk import pos_tag

nltk.download('punkt')

file=open(r"D:\DATA SCIENCE\Machine_learning\NLP2\assign\news_story.txt")

#here we first read all the text
text=file.read()
text
"""Out[50]: 'Inflation rose again in April, continuing a climb that has pushed consumers to the brink and is 
threatening the economic expansion, the Bureau of Labor Statistics reported Wednesday.\n\nThe consumer price 
index, a broad-based measure of prices for goods and services, increased 8.3% from a year ago, higher than the
 Dow Jones estimate for an 8.1% gain. That represented a slight ease from Marchâ€™s peak but was still close to
 the highest level since the summer of 1982.\n\nRemoving volatile food and energy prices, so-called core CPI still 
 rose 6.2%, against expectations for a 6% gain, clouding hopes that inflation had peaked in 
 March.\n\nThe month-over-month gains also were higher than expectations â€” 0.3% on headline CPI versus the
 0.2% estimate and a 0.6% increase for core, against the outlook for a 0.4% gain.\n\nThe price gains also meant 
 that workers continued to lose ground. Real wages adjusted for inflation decreased 0.1% on the month despite a 
 nominal increase of 0.3% in average hourly earnings. Over the past year, real earnings have dropped 2.6% even though 
 average hourly earnings are up 5.5%.\n\nInflation has been the single biggest threat to a recovery that began early 
 in the Covid pandemic and saw the economy in 2021 stage its biggest single-year growth level since 1984. Rising prices at the pump and in grocery stores have been one problem,
 but inflation has spread beyond those two areas into housing, auto sales and a host of other areas.\n\nFederal Reserve officials have responded to the problem with two interest rate hikes so far this year and pledges of more until inflation comes down to the central bankâ€™s 2% goal. 
 However, Wednesdayâ€™s data shows that the Fed has a big job ahead.\n\nCredits: cnbc.com'"""

#----------------------------------------tokenization
from nltk import word_tokenize
tokens = word_tokenize(text)

#-----------------------------------apply POS
tagged_tokens = pos_tag(tokens)
tagged_tokens
"""Out[54]: 
[('Inflation', 'NN'),
 ('rose', 'VBD'),
 ('again', 'RB'),
 ('in', 'IN'),
 ('April', 'NNP'),
 (',', ','),
 ('continuing', 'VBG'),
 ('a', 'DT'),
 ('climb', 'NN'),
 ('outlook', 'NN'),
 ('gains', 'NNS'),
 ('also', 'RB'),
 ('meant', 'VBP'),
 ('1984', 'CD'),"""
#-----------------------------------------extract NOUNs

#nouns = [word for word, pos in tagged_tokens if pos.startswith('N')]
nouns = [word for word, pos in tagged_tokens if pos=='NN']
nouns
"""['Inflation', 'April', 'climb', 'consumers', 'brink', 'expansion', 'Bureau', 'Labor', 'Statistics', 'Wednesday', 'consumer', 'price', 'index', 'measure', 'prices', 'goods', 'services', '%', 'year', 'Dow', 'Jones', 'estimate', '%', 'gain', 'ease', 'Marchâ€™s', 'peak', 'level', 'summer', 'food', 'energy', 'prices', 'core', 'CPI', '%', 'expectations', '%', 'gain', 
'hopes', 'inflation', 'March', 'gains', 'expectations', '%', 'headline', 'CPI', '%', 'estimate', '%', 'increase', 
'core', 'outlook', '%', 'gain', 'price', 'gains', 'workers', 'ground', 'wages', 'inflation', '%', 'month', 'increase', 
'%', 'earnings', 'year', 'earnings', '%', 'earnings', '%', 'Inflation', 'threat', 'recovery', 'Covid', 'pandemic', 
'economy', 'stage', 'growth', 'level', 'prices', 'pump', 'grocery', 'stores', 'problem', 'inflation', 'areas', 'housing', 'auto', 'sales', 'host', 'areas', 'Federal', 'Reserve', 'officials', 'problem', 'interest', 'rate', 'hikes', 'year', 'pledges', 'inflation', 'bankâ€™s', '%', 'goal', 'Wednesdayâ€™s', 'data', 'shows', 'Fed', 'job', 'Credits', 'cnbc.com']"""
    
#-----------------------------------------extract NOUNs all numbers (NUM POS type)
numbers = [word for word, pos in tagged_tokens if pos == 'CD']
numbers
"""Out[47]: 
['8.3',
 '8.1',
 '1982',
 '6.2',
 '6',
 '0.3',
 '0.2',
 '0.6',
 '0.4',
 '0.1',
 '0.3',
 '2.6',
 '5.5',
 '2021',
 '1984',
 'one',
 'two',
 'two',
 '2']"""
#---------------------------------------------Print a count of all POS tags in this story
pos_counts = nltk.FreqDist(pos for word, pos in tagged_tokens)
pos_counts
"""Out[49]: FreqDist({'NN': 70, 'IN': 39, 'DT': 34, 'NNS': 25, 'JJ': 20, 'CD': 19, 'RB': 15, 
'NNP': 15, ',': 13, 'VBD': 12, ...})"""