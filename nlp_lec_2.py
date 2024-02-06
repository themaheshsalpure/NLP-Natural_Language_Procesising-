# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 08:51:32 2023

@author: ASUS
"""

# 📌🐍--------------------------------------------------------------------------------------


from nltk.corpus import stopwords
stop_words = stopwords.words('English')            # fetching the stop words of english 
print(stop_words)

sentance = 'I am lerning NLP: It is one of the most popular library in python'

from nltk import word_tokenize

tokenized = nltk.word_tokenize(sentance)           # used to tokenize the given string / sentence
tokenized


# 📌🐍--------------------------------------------------------------------------------------


sentence_no_stops = " ".join([words for words in tokenized if words not in stop_words])
print(sentence_no_stops)


# 📌🐍--------------------------------------------------------------------------------------

sent = 'I visited MY from IND on 14-02-19'

normalized_sent = sent.replace('MY', 'Malaysia').replace('-19', '-2019').replace('IND','India')
normalized_sent

# 📌🐍--------------------------------------------------------------------------------------

"""

Using the Autocorrect library here 
This will autocorrect the wrongly apelled words using Speller module 

"""

from autocorrect import Speller     # autocorrect speller is used to correct the spelling of words that are spelled incorrectly 
spell = Speller(lang = 'en')        # inside speller specifying language 
word = spell('Englllish')
word

# 📌🐍--------------------------------------------------------------------------------------

"""
Using the autocorrect for the complete sentence 

"""
sentence = 'Naturral Langague processin deaals with the aartt of extaccting sentimments'

tokens = word_tokenize(sentence)
spelled = " ".join([spell(words) for words in tokens])
spelled

# 📌🐍--------------------------------------------------------------------------------------


import nltk
from nltk import PorterStemmer

stemmer = nltk.stem.PorterStemmer()
word = stemmer.stem("programming")           # Bringing word to its root format or base format using stemmer.stem function from porterstemmer 
word

# 📌🐍--------------------------------------------------------------------------------------

"""
Lemmetization of words - 

"""
nltk.download('wordnet')

from nltk.stem.wordnet import WordNetLemmatizer       
lemmetizer = WordNetLemmatizer()          # initializing WordNetLemmatizer 
lemmetizer.lemmatize('programmed')        # using lemmatization word is bringed to its base or dicctionry format 
lemmetizer.lemmatize('programs')
























