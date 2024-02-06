# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:50:35 2023

@author: ASUS
"""

📌🐍--------------------------------------------------------------------------------------

import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

📌🐍--------------------------------------------------------------------------------------

corpus = ['The mouse has a tiny little mouse','The cat saw the mouse','The cat cath the mouse','The end of mouse story']


📌🐍--------------------------------------------------------------------------------------


"""
Here we initialized the CountVectorizer as cv
"""
cv = CountVectorizer()


"""
Determining the word count using CountVectorizer from the corpus

"""
word_count = cv.fit_transform(corpus)
word_count.shape

📌🐍--------------------------------------------------------------------------------------


"""
Creating instance of TfidfTransformer and 
fed with the word count we got from the CountVectorizer
"""
tfid_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
tfid_transformer.fit(word_count)


📌🐍--------------------------------------------------------------------------------------


"""
Here we created the dataframe of the word tfid values which we got

"""
df_idf = pd.DataFrame(tfid_transformer.idf_,index=cv.get_feature_names_out(), columns=['idf_weights'])


"""
Here we sorted values in ascending order 
"""
x = df_idf.sort_values(by=['idf_weights'])
print(x)
