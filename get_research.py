import pybliometrics
# Document-specific information
# from pybliometrics.scopus import AbstractRetrieval
from pybliometrics.scopus import ScopusSearch
import pandas as pd

pybliometrics.scopus.init()

#1. search for articles by keywords
q_key1 = 'AUTHKEY(climate* OR "global warming")' # 
q_key2 = 'AUTHKEY( misinformation OR disinformation OR denial OR "fake news" OR skepticism OR conspiracy )'
q = q_key1 + ' AND ' + q_key2 + ' AND PUBYEAR < 2025'
s = ScopusSearch(q, subscriber=False)
print("search for articles")
# print(s)

# 2. save data to csv
df = pd.DataFrame(s.results)

filtered_df = df[df["subtype"] == "ar"]

filtered_df.to_csv("Scopus_climate_result_filtered.csv")

