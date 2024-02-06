# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:00:17 2023

@author: ASUS
"""

📌🐍--------------------------------------------------------------------------------------

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


corpus = ["At Least seven indian pharma companies are working to develop vaccine against the corona virus.This deadly virus that has infected more than 14 million globally',Bharat Biotech is the among the domestic pharma firm working on the corona virus vaccine in India"]

bag_of_words_model = CountVectorizer()
bow = bag_of_words_model.fit_transform(corpus).todense()
"""
Todense is used for removing the unwanted words from the corpus
"""


print(bow)

bag_of_words_df = pd.DataFrame(bow)
print(bag_of_words_df)

bag_of_words_df.columns = sorted(bag_of_words_model.vocabulary_)
bag_of_words_df.head()


📌🐍--------------------------------------------------------------------------------------

"""
Bag of words small model

Small model has the less vocabulary than the original 
"""

bag_of_words_model_small = CountVectorizer(max_features=5)
bag_of_words_df_small = pd.DataFrame(bag_of_words_model_small.fit_transform(corpus).todense())
bag_of_words_df_small

bag_of_words_df_small.columns = sorted(bag_of_words_model_small.vocabulary_)
bag_of_words_df_small


















