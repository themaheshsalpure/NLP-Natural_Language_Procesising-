# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:12:56 2023

@author: ASUS
"""

from sklearn.feature_extraction.text import TfidfVectorizer

corpus=[
        'Thor eating pizza, Loki is eating pizza, Ironman ate pizza already',
        'Apple is announcing ne iphone tommorow',
        'Tesla is announcing new model-3 tommorow',
        'Google is announcing new pixel-6 tommorow',
        'Microsoft is announcing new pixel-6 tommorow',
        'Amazon is announcing new eco-dot tommorow',
        'I am eating biryani and you are eating grapes']

v = TfidfVectorizer()
v.fit(corpus)

transform_output = v.transform(corpus)

print(v.vocabulary_)


all_feature_names = v.get_feature_names_out()
all_feature_names


for word in all_feature_names:
    
    """
    Here we get the index in in the vocabulary
    """
    index = v.vocabulary_.get(word)
    idf_score = v.idf_[index]
    print(f"{word} : {idf_score}")





