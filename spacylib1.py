import spacy

# nlp = spacy.load("en_core_web_sm")
# doc = nlp('Dr. strange likes Mumbai wadapaw. Hulk loves chaat of delhi.')

# for sentence in doc.sents:
#     print(sentence)

nlp = spacy.blank('en')

doc = nlp('Dr. Strange likes Mumbai wadapaw. Hulk loves chaat of Delhi.')
doc1 = nlp("'Let's go to N.Y.!'")


for token in doc1:
    print(token)

# print(doc[0])