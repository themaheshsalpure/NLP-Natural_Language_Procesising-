# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:24:13 2023

@author: ASUS
"""


#📌🐍 -------------------------------------------------------------------------
 
string1 = 'Apple'
string2 = 'jeeil123'
string3 = '12345'
string4 = 'pre@12'

x = string1.encode(encoding='UTF8', errors='strict')    # Encoding given characters and if there is any char which cant be encoded then will raise the error
print(x)
y = string2.encode(encoding = 'UTF8', errors='strict')  # UTF 8 (Unicode Trnasformation Format 8) - character encoding standard 
print(y)
z = string3.encode(encoding='UTF8', errors='strict')
print(z)
a = string4.encode(encoding='UTF8', errors='strict')
print(a)





#📌🐍 -------------------------------------------------------------------------

text = 'one 🐘 and three 🐋'

x = text.encode(encoding='UTF8', errors='strict')
print(x)



with open('data.txt',mode = 'rb') as f:            # Opening data.txt in read binary format as f 
    x =f.read()
    print(x)

print(x.decode(encoding='UTF8'))                   # Decoding file using UTF 8 standard 


#📌🐍 ------------------------------------------------------------------
'''
removing the extra spaces using strip() function

'''


x = '  hello '

z = x.strip()      # both side void space will be removed
print(z)

a = x.lstrip()      # left side void space is going to removed
print(a)

b =x.rstrip()       # right side void space is going to removed
print(b)


'''
removing any specific type of characters from string
'''
x = '-------Hello==='

a = x.lstrip('-')
print(a)

b = x.strip('-=')
print(b)



#📌🐍 -------------------------------------------------------------------------
'''
replacing the space with the no space

'''

x = '     hello   world   '

a = x.replace(" ","")          # removing space from string by using replace function 
print(a)




#📌🐍 -------------------------------------------------------------------------

'''
removing the space 
'''

import re

x = '     Hello  world   '
y = re.sub(r'\s+', '', x)            # remiving space from string using regex sub function
print(y)


#📌🐍 -------------------------------------------------------------------------

'''
Alligning the text 

'''

x = 'Hello World'      # ljust() is used for lefft justify 
a = x.ljust(20, '=')   # Will make pedding 20 for this string 20-11=9 hence will add 9 '=' in right side 
print(a)

b = x.rjust(30, '=')   # right justify by adding 9 '=' in left side 
print(b)

c = x.center(20, '=')  # this will center justify by adding '=' in left and right side of string
print(c)



#📌🐍 -------------------------------------------------------------------------


x = 'Hello world'

a = format(x, '>20')
print(a)

b = format(x, '<20')
print(b)

c = format(x, '^20')
print(c)


d = format(x, '=>20')
print(d)

e = format(x, '*^20')
print(e)

a= '{:>10s}{:>10s}'.format('Hello', 'world')
print(a)


x = 1.2345

format(x, '^10.2f')



parts = ['is','chicago','Not','Chicago ?']
x = " ".join(parts)               # Used to form string from list 
print(x)


parts = ['is','chicago','Not','Chicago ?']
x = "=".join(parts)                # will join all the data from list by using '=' seperator
print(x)
























































