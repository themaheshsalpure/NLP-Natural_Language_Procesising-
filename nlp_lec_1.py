# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:26:15 2023

@author: ASUS
"""


# 📌🐍--------------------------------------------------------------------------------------

"""
Here finding the index of the Learning word by using charcter position 
"""

sentence = "We are learning TextMining from Sanjivani AI"

sentence.index("learning")


# 📌🐍--------------------------------------------------------------------------------------

"""
Here first performing the splitting of word into tokens and then finding the 
index of the word 'TextMining' which is 3
first it will create an list of tokens of words and then it will search for the
position of the word in that list.

"""
splitted = sentence.split()
splitted.index('TextMining')

sentence.split().index('TextMining')


# 📌🐍--------------------------------------------------------------------------------------


"""
Reversing the string 

"""

sentence = "We are learning TextMining from Sanjivani AI"

sentence.split()[2][::-1]

# Reversing the TextMining word
sentence.split()[3][::-1]



# 📌🐍--------------------------------------------------------------------------------------

"""
Getting the first and last word of the string 

"""

first_word = sentence.split()[0]
first_word

last_word = sentence.split()[-1]
last_word


# 📌🐍--------------------------------------------------------------------------------------


concat_word = first_word+" "+last_word
concat_word


# 📌🐍--------------------------------------------------------------------------------------

words = sentence.split()

[words[i] for i in range(len(words)) if i%2==0]



# 📌🐍--------------------------------------------------------------------------------------

sentence.split()[-1:]


# 📌🐍--------------------------------------------------------------------------------------

sentence[::-1]


# 📌🐍--------------------------------------------------------------------------------------

"""
Reversing the each word in the sentence
"""

words = " ".join(word[::-1] for word in words)
words



# 📌🐍--------------------------------------------------------------------------------------

import nltk

stemmer = nltk.PorterStemmer()
tokenized = stemmer.stem(sentence)

tokenized


nltk.download('punkt')

from nltk import word_tokenize
word = word_tokenize("I am reading NLPfundamentals")
word

nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger')



import nltk
nltk.download('all')









