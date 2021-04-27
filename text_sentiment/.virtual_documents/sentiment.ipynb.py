import spacy



nlp = spacy.load('en_core_web_sm')


######cleaning


text = "she is a bitch"


#####cleaning
import string
punt =set(string.punctuation)
email=r'\S+@\S+'
urls = r'http\S+'
import re
text=re.sub(email,'',text)
text=re.sub(urls,'',text)

doc = nlp(text)
doc_c = []
doc_c = [token.lemma_ for token in doc if token.text.lower() not in punt and not token.is_stop and token.is_alpha]
doc_c_s = ' '.join(doc_c)


import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentiment_analyser  = SentimentIntensityAnalyzer()
dic = sentiment_analyser.polarity_scores(doc_c_s)
print(max(dic,key = lambda x:dic[x]))


for x in dic:
    print(x,dic[x])







