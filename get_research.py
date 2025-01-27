import pybliometrics
# Document-specific information
# from pybliometrics.scopus import AbstractRetrieval
from pybliometrics.scopus import ScopusSearch
import pandas as pd

pybliometrics.scopus.init()

#1. search for articles by keywords
q = '(AUTHKEY("climate change" OR "global warming" OR "environmental change") AND AUTHKEY(misinformation OR disinformation OR denial OR "fake news" OR skepticism OR skeptic)) AND LIMIT-TO(DOCTYPE, ar)'
s = ScopusSearch(q, subscriber=False)
print("search for articles")
# print(s)

# 2. save data to csv
df = pd.DataFrame(s.results)

df.to_csv("Scopus_articles_result_author.csv")

