# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:23:08 2023

@author: ASUS
"""



#📌🐍 ------------------------------------------------------------------

# tokenization

data = 'Welcome to the new year 2023'

x = data.split()
print(x)


#📌🐍 ------------------------------------------------------------------

'''
removing the special characters 
'''

'''
the pattern we used in the function re.sub() is used to ignore that characters passed in that
function and from the string thaat characters are ignored and remaining characters are removed
from the string and the string is returned 

'''

import re

data = '''007 not sure@ if thi7s % was #fun ! 
589848 what do you? think* of it #7756@8
'''

'''
from above string the folowing characters are ignored and the remaining characters are removed
'''

pattern = r'[^a-zA-Z0-9.,:;\"\'\s]'

def info(pattern, data):
    # x = re.findall(pattern, data)
    return re.sub(pattern, '', data)
    # return x

print(info(pattern, data))




#📌🐍 ------------------------------------------------------------------
#📌🐍 ------------------------------------------------------------------



'''
removing the punctuation from the sentence 

'''
import string 
def remove_punctuation(data):
    text = ''.join([c for c in data if c not in string.punctuation])
    return text 

x = '''Article: @ first sentence of some, 
{important} article having a lot of ~ punctuations and another one ; !'''

print(remove_punctuation(x))





#📌🐍 ------------------------------------------------------------------


import nltk


data ='we are eating and swimming ; we have been eating and swimming ; we have been ate and swam'
def info(data):
    stemmer = nltk.PorterStemmer()
    text = ' '.join([stemmer.stem(word) for word in data.split()])
    return text



print(info(data))


#📌🐍 ------------------------------------------------------------------


import re

data = 'asdf fjkd; afed, fjek,asdf, foo'

x = re.split(r'(?:,/;/\s)\s*', data)
print(x)
txt= 'asdf fjkd; afed, fjek,asdf, foo'

pattern = r'(?:,/;/\s)\s*'
x = re.split(pattern, txt)    
print(x)



#📌🐍 ------------------------------------------------------------------


'''

using startwith and endswith

'''

filename = 'spam.txt'

x = filename.endswith('.txt')
print(x)



#📌🐍 ------------------------------------------------------------------


choices = ('http:','ftp:')
url = 'http://www.python.org'
x = url.startswith(choices)
print(x)


#📌🐍 ------------------------------------------------------------------

'''
string slicing and indexing 
'''

s = 'ABCDEFGHI'
print(s[2:7])   # positive


print(s[::-1])   # reverse

print(s[-7:-3])     # reverse/negative

print(s[2:-5])  # positive and negative mix

print(s[::2])   # slicing in two steps

print(s[6:1:-2])

print(s[6:])

print(s[::-1])

filename = 'spam.txt'
print(filename[-4:] == ".txt")


url = 'htpps://www.instagram.com'

x = (url[:5]=='http' or url[:6]=="https:" or url[:4]=='ftp')
print(x)


#📌🐍 ------------------------------------------------------------------


from fnmatch import fnmatch ,fnmatchcase

names = ['Dat1.csv','Dat2.csv', 'config.ini', 'foo.py']

x = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(x)


#📌🐍 ------------------------------------------------------------------

from fnmatch import fnmatch, fnmatchcase

addr = ['3463 n clark st','753 w addison st','343 r snada ave', '7823 astagaon est']

x = [name for name in addr if fnmatchcase(name, '* st')]
print(x)


#📌🐍 ------------------------------------------------------------------


from fnmatch import fnmatch, fnmatchcase

text = 'yeah, but no, but yeah, but no, but yeah'

x = text.startswith('yeah')
print(x)

y = text.endswith('no')
print(y)



#📌🐍 ------------------------------------------------------------------

'''
using .match() from re

'''

import re

text1 = '11/03/2023'

if re.match(r'\d+/\d+/\d+', text1):
    print('Yes')
else :
    print('No')

import re

text1 = '11/03/2023'
def match(text):
    if re.findall(r'\d+/\d+/\d', text):
        return 'Yes'
    else :
        return 'NO'

print(match(text1))


#📌🐍 ------------------------------------------------------------------


import re
text1 = '11/03/2023'
data = re.compile(r'(\d+)/(\d+)/(\d+)')
print(data)
if re.match(data, text1):
    print("Yes")
else :
    print("No")


#📌🐍 ------------------------------------------------------------------


data = 'yeah, but no, but yeah, but no, but yeah'
x  = data.replace('yeah','yupp')
print(x)


#📌🐍 ------------------------------------------------------------------
'''

changing positions and replacing values

'''


data = 'Today is 11/27/2012. pycon starts 3/13/2024'

import re
x = re.sub('(\d+)/(\d+)/(\d+)', r'\3-\1-\2', data)
print(x)

#📌🐍 ------------------------------------------------------------------

import re
data = 'Upper PYTHON, lower python, mixed Python'

x = re.findall('python', data, flags = re.IGNORECASE)
print(x)

y = re.sub('python', 'snake',data, flags = re.IGNORECASE)
print(y)



#📌🐍 ------------------------------------------------------------------



import re


text = 'Upper PYTHON, lower python, mixed Python'

def matchcase(word):
    def replace(m):
        text = m.group()
        
        '''
        text = m.group() is used to match the matched words from text and giving that
        matches into the text and then comparing the value of m (i.e. snake) and changing 
        that word according to the text(i.e. matched word)
        
        '''
        
        
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else :
            return word
    return replace
text3 = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(text3)



#📌🐍 ------------------------------------------------------------------



x = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
x = re.findall(text)
print(x)


#📌🐍 ------------------------------------------------------------------



s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)

s1 == s2




































