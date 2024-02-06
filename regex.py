# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:41:52 2023

@author: ASUS
"""

#📌🐍--------------------------------------------------------------------------------------

'''
Extracting the 10 digit number from the string by using the 10*\d as pattern 
got paattern from regex101.com

we extracted the indian type of mobile number 
'''
import re

text = '''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. 
        Tesla's revenue is 40 billion Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 
        billio'''
        
pattern = '\d\d\d\d\d\d\d\d\d\d'

matches = re.findall(pattern, text)
print(matches)


# using another type of pattern

import re

text = '''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern = '\d{10}'

matches = re.findall(pattern, text)
print(matches)




#📌🐍--------------------------------------------------------------------------------------




'''
finding/ extracting the us type of number from the string 
number as =  (999)-333-7777 

'''


import re

text ='''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern = "\(\d{3}\)\-\d{3}\-\d{4}"

matches = re.findall(pattern, text)
print(matches)




#📌🐍--------------------------------------------------------------------------------------



'''
finding the both type of the numbers at once
'''

import re

text = '''Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern = "\(\d{3}\)\-\d{3}\-\d{4} | \d{10}"

matches = re.findall(pattern, text)
print(matches)



 
#📌🐍--------------------------------------------------------------------------------------



'''
Text - 
    A protracted; legal battle; over a 32-carat;
    Golconda diamond-
    
    
IF we want to clean this text and dont want that colon and hyphen pattern in that text 
then we can do this using following technique
'''


import re

text1 = '''A protracted; legal battle; over a 32-carat;
 Golconda diamond-'''

pattern = '[^;-]'

matches = re.findall(pattern, text1)
print(matches)



#📌🐍--------------------------------------------------------------------------------------

'''
Extracting the speecific part of the paragraph from the para. 
Here we want only the first line of the paragraph 

'''
import re

text = '''Note 1 – Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.'''



pattern = 'Note \d – [^\n]+'
match = re.findall(pattern, text)

print(match)



#📌🐍--------------------------------------------------------------------------------------

'''
trying to get only the 'Summary of Significant Accounting Policies'
from the paragraph
'''

import re

text = '''Note 1 – Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.'''

pattern = 'Note \d – ([^\n]+)'

x = re.findall(pattern, text)
print(x)




#📌🐍--------------------------------------------------------------------------------------


import re
import pandas as pd

data = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. '''

pattern = 'FY\d{4} Q\d'

x = re.findall(pattern, data)
print(x)

# converting data into tabple of dataframe

l = len(x)
l
f = []
for i in range(l):
    z = x[i].split()
    f.append(z)
    
print(f)
y = pd.DataFrame(f)
print(y)



'''
this is another way of the pattern for the same result 
'''
import re

data = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. '''

pattern = "FY\d{4} Q[1234]"

x = re.findall(pattern, data)
print(x)


'''
this is third type of the way for getting the same result 
'''
import re

data = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. '''

pattern = "FY\d{4} Q[1-4]"

x = re.findall(pattern, data)
print(x)


#📌🐍--------------------------------------------------------------------------------------

'''
using the re.IGNORECASE by which we will get capital FY as well as small fy

'''

import re

data = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. '''

pattern = "FY\d{4} Q[1-4]"

x = re.findall(pattern, data, re.IGNORECASE)
print(x)


# using the or condition in the pattern 

import re

data = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. '''

pattern = "fy\d{4} Q[1-4] | FY\d{4} Q[1-4]"

x = re.findall(pattern, data)
print(x)



#📌🐍--------------------------------------------------------------------------------------

'''
ignoring the fy any only getting the year and q value

'''

import re

data = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. '''

pattern = "FY(\d{4} Q[1-4])"

x = re.findall(pattern, data)
print(x)





#📌🐍--------------------------------------------------------------------------------------

'''
$ and "." is a special char hence while extracctin these characters we first have
to use \ 

'''

import re

data = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. '''

pattern = "\$\d\.\d{2}"

x = re.findall(pattern, data)
print(x)




import re

data = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. '''

pattern = "\$[0-9\.]+"

x = re.findall(pattern, data)
print(x)




#📌🐍--------------------------------------------------------------------------------------



'''
Reading the pdf file for nlp from our internal drive

'''

from PyPDF2 import PdfFileReader as pr

from PyPDF2 import PdfReader as pd

data = pd('python_tutorial.pdf')

# finding the number of the pages in the pdf
x = len(data.pages)

# we accessed the specific page (page 10) using this line
x = data.pages[20]
print(x)

# extracted the text data from that page
text = x.extract_text()
print(text)



#📌🐍--------------------------------------------------------------------------------------


# using first type of the pattern 
import re
data = 'I have a problem with my order number 4412889912'
pattern = 'order number ([^\n]+)'

x = re.findall(pattern, data)
print(x)

# using another pattern
import re
data = 'I have a problem with my order number 9673912364 and 4412889912 is my phone number'
pattern = 'order[^\d]+(\d*)'

x = re.findall(pattern, data)
print(x)


'''
changing the pattern of the data

'''
import re

data = 'My order 4412889912 is having some issue'
pattern = 'order[^\d]+(\d*)'
x = re.findall(pattern, data)
print(x)


import re

data = 'hey , hello My order is 4412889912 and it is having some issue'
pattern = 'order[^\d]+(\d*)'
x = re.findall(pattern, data)
print(x)


"""
writing the function for the pattern match
"""
import re

def match(pattern, data):
    x = re.findall(pattern, data)
    if x:
        return x[0]


data = 'hey , hello 4412889912 is My order number and it is having some issue'
y  = match('([\d]+)', data)
print(y)




'''
extracting the email ids from the given data

'''

import re

def match(pattern, data):
    x = re.findall(pattern, data)
    if x:
        return x[0]

chat1 = "Hi, you ask lot of questions 123456789 xyz@gmail.com"
chat2 = "Hi: here it is : (123)-456-7890 xyz@gmail.com"
pattern = "[a-zA-Z0-9]*@[a-z]*\.[a-z]*"

x = match(pattern, chat1)
print(x)

y = match(pattern, chat2)
print(y)




#📌🐍--------------------------------------------------------------------------------------



'''
extracting the date of birth from the data
full name and the age of the person from the data

'''

import re

text ='''Elon Reeve Musk is a business magnate and investor. Musk is the founder, chairman, CEO and chief technology officer of SpaceX, angel investor, CEO and product architect of Tesla, Inc., owner, chairman ... Wikipedia
Born: 28 June 1971 (age 52 years), Pretoria, South Africa
Net worth: 22,340 crores USD (2023) Forbes
Children: Vivian Jenna Wilson, Nevada Alexander Musk, Griffin Musk, Damian Musk, Kai Musk, Saxon Musk
Spouse: Talulah Riley (m. 2013–2016), Talulah Riley (m. 2010–2012), Justine Musk (m. 2000–2008)
Full name: Elon Reeve Musk
Parents: Errol Musk, Maye Musk'''


pattern = "Born[^\d]*([0-9]* [a-zA-Z]* [0-9]*)"
pattern1 = "Elon [a-zA-Z]* [a-zA-Z]*"
pattern2 = "age ([0-9]* [a-zA-Z]*)"


def match(pattern, data):
    x = re.findall(pattern, data)
    if x :
        return x[0]

y = match(pattern, text)
print(f"Born on : {y}")
z = match(pattern1, text)
print(f"Full name is : {z}")
a = match(pattern2, text)
print(f"Age is : {a}")


#📌🐍--------------------------------------------------------------------------------------




import re

text ='''Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[2]
Parents	
Errol Musk
Maye Musk
Family	Musk family'''


pattern = "June [0-9]*, [0-9]*"


def match(pattern, data):
    x = re.findall(pattern, data)
    if x :
        return x[0]

y = match(pattern, text)
print(f"{y}")



#📌🐍--------------------------------------------------------------------------------------
'''

converting the extractedd data into the dictionary

'''

import re

text ='''Elon Reeve Musk is a business magnate and investor. Musk is the founder, chairman, CEO and chief technology officer of SpaceX, angel investor, CEO and product architect of Tesla, Inc., owner, chairman ... Wikipedia
Born: 28 June 1971 (age 52 years), Pretoria, South Africa
Net worth: 22,340 crores USD (2023) Forbes
Children: Vivian Jenna Wilson, Nevada Alexander Musk, Griffin Musk, Damian Musk, Kai Musk, Saxon Musk
Spouse: Talulah Riley (m. 2013–2016), Talulah Riley (m. 2010–2012), Justine Musk (m. 2000–2008)
Full name: Elon Reeve Musk
Parents: Errol Musk, Maye Musk'''


def match(pattern, data):
    x = re.findall(pattern, data)
    if x :
        return x[0]

def info(text): 
    dob = match('Born[^\d]*([0-9]* [a-zA-Z]* [0-9]*)', text)
    name = match('Elon [a-zA-Z]* [a-zA-Z]*', text)
    age = match('age ([0-9]* [a-zA-Z]*)', text)
    return {
        'name':name.strip(),
        'age':age.strip() ,
        'Date of birth' :dob.strip()
        }
print(info(text))    



#📌🐍--------------------------------------------------------------------------------------

'''
extracting the information of the mukesh ambani

'''

import re

data = '''Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 66)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)'''



def match(pattern, data):
    x = re.findall(pattern, data)
    if x :
        return x[0]

def info(data):
    name = match('Born(.*[^\n])',data)
    age = match("age ([0-9]*)", data)
    nationality = match('Nationality(.*[^\n])', data)
    spouse = match('Spouse	([a-zA-Z]* [a-zA-Z]*)', data)
    return {
        'Name' : name.strip(),
        'Age' : age.strip(),
        'Nationality' : nationality.strip(),
        'Spouse' : spouse.strip()
        }   
print(info(data))











