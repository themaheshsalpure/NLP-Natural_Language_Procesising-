# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:24:02 2023

@author: jwark
"""
#--------------------------------------Pattern matching using tokrnization

"""Problem statement: 
text='''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.

Using tokenization , Extract all money transaction from below sentence along with currency. Output should be,
wo $
500 €
"""
from nltk.tokenize import RegexpTokenizer
# Extract all money transaction from below sentence along with currency.
text='''Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.wo $500 €'''

reg_tokenizer=RegexpTokenizer('\$\d+')
reg_tokenizer.tokenize(text)
#Out[4]: ['$500']

########################################################################################

#--------------------------------Steaming

"""
Problem statement: 
1.Use stemming for following docs
doc = nlp("Mando talked for 3 hours although talking isn't his thing")
doc = nlp("eating eats eat ate adjustable rafting ability meeting better")
"""

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt')

doc1 = "Mando talked for 3 hours although talking isn't his thing"

#convert doc into tokens
tokens = word_tokenize(doc1)
tokens
"""['Mando',
 'talked',
 'for',
 '3',
 'hours',
 'although',
 'talking',
 'is',
 "n't",
 'his',
 'thing']"""

# Initialize Porter Stemmer
porter_stemmer = PorterStemmer()

# Apply stemming to each token
stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]
stemmed_tokens
"""['mando',
 'talk',
 'for',
 '3',
 'hour',
 'although',
 'talk',
 'is',
 "n't",
 'hi',
 'thing']"""

# Join the stemmed tokens back into a string
stemmed_text = ' '.join(stemmed_tokens)
stemmed_text
#Out[36]: "mando talk for 3 hour although talk is n't hi thing"

# Print the stemmed documents
print("Original Document:", doc1)
#Original Document 1: Mando talked for 3 hours although talking isn't his thing
print("Stemmed Document:", stemmed_text)
#Stemmed Document 1: mando talk for 3 hour although talk is n't hi thing


doc2 = "eating eats eat ate adjustable rafting ability meeting better"
print("\nOriginal Document 2:", doc2)
print("Stemmed Document 2:", stemmed_text)

#---------------for second sentense 

doc2 = "eating eats eat ate adjustable rafting ability meeting better"

#convert doc into tokens
tokens = word_tokenize(doc2)
tokens
"""['eating',
 'eats',
 'eat',
 'ate',
 'adjustable',
 'rafting',
 'ability',
 'meeting',
 'better']"""

# Initialize Porter Stemmer
porter_stemmer = PorterStemmer()

# Apply stemming to each token
stemmed_tokens = [porter_stemmer.stem(token) for token in tokens]
stemmed_tokens
"""Out[44]: ['eat', 'eat', 'eat', 'ate', 'adjust', 'raft', 'abil', 'meet', 'better']"""

# Join the stemmed tokens back into a string
stemmed_text = ' '.join(stemmed_tokens)
stemmed_text
#Out[46]: 'eat eat eat ate adjust raft abil meet better'

# Print the stemmed documents
print("Original Document:", doc2)
#Original Document: eating eats eat ate adjustable rafting ability meeting better
print("Stemmed Document:", stemmed_text)
#Stemmed Document: eat eat eat ate adjust raft abil meet better

###############################################################################################################