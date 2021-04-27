[![NLTK](https://img.shields.io/badge/NLTK-3.6.2-brightgreen)](https://www.nltk.org/)
[![pandas](https://img.shields.io/badge/pandas-1.2.4%20-green)](https://pandas.pydata.org/)
[![numpy](https://img.shields.io/badge/numpy%20-1.20.2%20-yellowgreen)](https://numpy.org/)
[![PIL](https://img.shields.io/badge/pillow-%208.2.0%20-yellow)](https://pypi.org/project/Pillow/)
[![pip](https://img.shields.io/badge/pip-21.0.1%20-orange)](https://pypi.org/project/pip/)
[![python](https://img.shields.io/badge/python%20-3.8.8%20-red)](https://www.python.org/)
[![regex](https://img.shields.io/badge/regex%20-2021.4.4%20-lightgrey)](https://regexr.com/)
[![Spacy](https://img.shields.io/badge/spacy-3.0.6-blue)](https://spacy.io/)
[![streamlit](https://img.shields.io/badge/streamlit-%200.80.0-brightgreen)](https://streamlit.io/)
[![Textblob](https://img.shields.io/badge/textblob%20-0.15.3%20%20-yellow)](https://textblob.readthedocs.io/en/dev/)
--------------------------------
# NLP-App-Streamlit
A Natural language processing app for sentiment analysis , text summarization ,language  translation , language identification 
### Features
  - uses vader sentiment analysis to show positive ,negative ,neutral sentiment.
  
  - Gensim summarizer for producing summary .
  
  - Textblob and Google API for language translation and identification.
------------------------ 
### How to run locally
##### 1.install [anaconda](https://www.anaconda.com/products/individual) in your system 
   
  `pip install -r requirements.txt`
  
  `python -m spacy download en_core_web_sm`
  
  `streamlit run main.py`
