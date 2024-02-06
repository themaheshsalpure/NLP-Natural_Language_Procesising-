# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:52:16 2023

@author: jwark
"""
#----------------------lemitization and steaming
"""
Problem statement:
convert these list of words into base form using Stemming and Lemmatization and observe the transformations 
 
#using stemming in nltk
lst_words = ['running', 'painting', 'walking', 'dressing', 'likely', 'children', 'whom', 'good', 'ate', 'fishing']
#using lemmatization in spacy
doc = nlp("running painting walking dressing likely children who good ate fishing")

'''
"""

#import lib
from nltk.stem import PorterStemmer

#using stemming in nltk
lst_words = ['running', 'painting', 'walking', 'dressing', 'likely', 'children', 'whom', 'good', 'ate', 'fishing']

#initialize portstemmer()
steam=PorterStemmer()

#steamed the words
stemmed_words = [steam.stem(i) for i in lst_words]
stemmed_words
"""Out[54]: 
['run',
 'paint',
 'walk',
 'dress',
 'like',
 'children',
 'whom',
 'good',
 'ate',
 'fish']"""
#here in steamed words ing removes from original words.

#---------------------lemitization
"""
Problem statement:
convert these list of words into base form using Stemming and Lemmatization and observe the transformations 
#using lemmatization in spacy
doc = nlp("running painting walking dressing likely children who good ate fishing")

'''
"""
import nltk
from nltk import word_tokenize
from nltk import WordNetLemmatizer
nltk.download('wordnet')
lemma=WordNetLemmatizer()

doc ="running painting walking dressing likely children who good ate fishing"
tokenn=word_tokenize(doc)

lemitize_word=[lemma.lemmatize(i) for i in tokenn]
lemitize_word
"""Out[73]: 
['running',
 'painting',
 'walking',
 'dressing',
 'likely',
 'child',
 'who',
 'good',
 'ate',
 'fishing']"""
#############################################################################################################3

#--------------steam and lemitize sentense
"""
Problem statement:

3.convert the given text into it's base form using both stemming and lemmatization
text = '''Latha is very multi talented girl.She is good at many skills like dancing, running, singing, playing.She also likes eating Pav Bhagi. she has a 
habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
'''
"""
from nltk import PorterStemmer
from nltk import tokenize
steamm=PorterStemmer()
text = '''Latha is very multi talented girl.She is good at many skills like dancing, running, singing, playing.She also likes eating Pav Bhagi. she has a 
habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
'''

#---------------------------tokenization
k=tokenize.word_tokenize(text)
k
"""Out[6]: 
['Latha',
 'is',
 'very',
 'multi',
 'talented',
 'girl.She',
 'is',
 'good',
 'at',
 'many',
 'skills',
 'like',
 'dancing',
 ',',
 'running',
 ',',
 'singing',
 ',',
 'playing.She',
 'also',
 'likes',
 'eating',
 'Pav',
 'Bhagi',
 '.',
 'she',
 'has',
 'a',
 'habit',
 'of',
 'fishing',
 'and',
 'swimming',
 'too.Besides',
 'all',
 'this',
 ',',
 'she',
 'is',
 'a',
 'wonderful',
 'at',
 'cooking',
 'too',
 '.']"""

#--------------------steaming
#here we steamed the words
steaming_words=[steamm.stem(i) for i in k]

steaming_sentence=' '.join(steaming_words)
steaming_sentence
"""Out[15]: 'latha is veri multi talent girl.sh is good at mani skill like danc , run , 
sing , playing.sh also like eat pav bhagi . she ha a habit of fish and swim too.
besid all thi , she is a wonder at cook too .'"""

#----------------lemitization
import nltk
from nltk import WordNetLemmatizer
lemma=WordNetLemmatizer()
nltk.download('wordnet')
lemitize_word=[lemma.lemmatize(i) for i in k]
lemitize_word
lemitize_sentence=' '.join(lemitize_word)
lemitize_sentence
"""Out[26]: 'Latha is very multi talented girl.She is good at many skill like dancing , running , 
singing , playing.She also like eating Pav Bhagi . she ha a habit of fishing and swimming too.
Besides all this , she is a wonderful at cooking too .'"""

#######################################################################################################