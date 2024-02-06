# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 08:37:29 2023

@author: ASUS
"""
📌🐍--------------------------------------------------------------------------------------


sentance = "Sentence tokenization is the process of splitting text into individual sentences"
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentance)


📌🐍--------------------------------------------------------------------------------------


from textblob import TextBlob
blob = TextBlob(sentance)
blob.words


📌🐍--------------------------------------------------------------------------------------


from nltk.tokenize import TweetTokenizer
tokenizer = TweetTokenizer()
tokenizer.tokenize(sentance)


📌🐍--------------------------------------------------------------------------------------

sen = 'Sentence tokenization is the process of;splitting text into individual sentences'
from nltk.tokenize import MWETokenizer
mwt = MWETokenizer([('splitting','text')])
mwt.tokenize(sentance.split())
mwt.tokenize(sentance.replace(";"," ").split())


📌🐍--------------------------------------------------------------------------------------


"""

code Didnt run Properly ---------------------------------------


"""


sentance5 = "Sharat tweeted ,witnessing 70th republic day. India from Rajpath \New Delhi Mesmorizing performance by Indian army."

from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
tokenizer.tokenize(sen)


📌🐍--------------------------------------------------------------------------------------

from nltk.tokenize import WhitespaceTokenizer

tokenizer = WhitespaceTokenizer()
tokenizer.tokenize(sen)


📌🐍--------------------------------------------------------------------------------------


from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
tokenizer.tokenize(sen)


📌🐍--------------------------------------------------------------------------------------

sentance6 = 'I love playing cricket. Cricket player practices hard in their training'

from nltk.stem import RegexpStemmer

stemmer = RegexpStemmer('ing$')
stem = ' '.join(stemmer.stem(wd) for wd in sentance6.split())
stem

📌🐍--------------------------------------------------------------------------------------


sent = 'Before eating, it would be nice to sanitize your hands'


from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
# stemmer.stem(sent)
words = ' '.join(stemmer.stem(wd) for wd in sent.split())
words


📌🐍--------------------------------------------------------------------------------------

------------------- Lemmetization --------------------------

import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize

nltk.download('wordnet')

lemmetizer = WordNetLemmatizer()
sentance7 = "The codes executed today are far better than wht we execute generally."
wtokenizer = word_tokenize(sentance7)
op = ' '.join([lemmetizer.lemmatize(word) for word in wtokenizer])
op 


📌🐍--------------------------------------------------------------------------------------

from textblob import TextBlob
 
sent1 = 'She sells seashells on the seashore'
word = TextBlob(sent1)
word.words

# this is used to singularize the plural word
word.words[2].singularize()

# This will pluralize the singular word
word.words[5].pluralize()


📌🐍--------------------------------------------------------------------------------------

from textblob import TextBlob

bword = TextBlob(u'muy bien')
w = bword.translate(from_lang = 'es', to = 'en')
w

📌🐍--------------------------------------------------------------------------------------

from nltk import word_tokenize

sent1 = 'She sells seashells on the seashore'

stop_word = ['she','on','the','am''is']
word = word_tokenize(sent1)


new = ' '.join([words for words in word if words not in stop_word])
new

"""
here first we splitted words using the word_tokenize function and then we extracted the 
words form the sentance which are not in the stop words list and taken only those numbers
using list comprehension.

"""
📌🐍--------------------------------------------------------------------------------------

























