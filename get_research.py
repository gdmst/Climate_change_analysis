import pybliometrics
# Document-specific information
# from pybliometrics.scopus import AbstractRetrieval
from pybliometrics.scopus import ScopusSearch
import pandas as pd

pybliometrics.scopus.init()

#1. search for articles by keywords
q = '(KEY("climate change" OR "global warming" OR "environmental change") AND KEY(misinformation OR disinformation OR denial OR "fake news" OR skepticism)) AND LIMIT-TO(DOCTYPE, ar)'
s = ScopusSearch(q, subscriber=False)
print("search for articles")
# print(s)


# 2. save data to csv
df = pd.DataFrame(s.results)

df.to_csv("Articles_result.csv")


# ab = AbstractRetrieval("10.1016/j.softx.2019.100263")
# print("Abstract retrieval")
# print(ab.title)
# print("publication name" + ab.publicationName)
# # print("author" + ab.authors)


# # Author-specific information
# from pybliometrics.scopus import AuthorRetrieval
# au2 = AuthorRetrieval(ab.authors[1].auid)
# print(au2.h_index)
# au1 = AuthorRetrieval(ab.authors[0].auid)
# print(au1.affiliation_current)

# # Affiliation information
# from pybliometrics.scopus import AffiliationRetrieval
# aff1 = AffiliationRetrieval(au1.affiliation_current[0].id)
# print(aff1.author_count)

# https://www.scopus.com/results/results.uri?sort=plf-f&src=s&sid=e6b374eec87b8c78009095241e6ecfd6&sot=a&sdt=a&cluster=scosubtype%2C%22ar%22%2Ct&sl=150&s=%28KEY%28%22climate+change%22+OR+%22global+warming%22+OR+%22environmental+change%22%29+AND+KEY%28misinformation+OR+disinformation+OR+denial+OR+%22fake+news%22+OR+skepticism%29%29&origin=searchadvanced&editSaveSearch=&txGid=b17d9a919536f80a5d4d51ef27f6e9cf&sessionSearchId=e6b374eec87b8c78009095241e6ecfd6&limit=10