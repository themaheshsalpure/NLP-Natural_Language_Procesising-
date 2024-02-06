import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


str = "Dr. strange loves Mumbai wada Pao. Hulk loves chaat of delhi  !"

op = sent_tokenize(str)

wop = word_tokenize(str)


print(op)

print(wop)