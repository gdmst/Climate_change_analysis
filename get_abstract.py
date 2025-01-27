import pybliometrics
from pybliometrics.scopus import AbstractRetrieval
import pandas as pd
pybliometrics.scopus.init()

list = []

df = pd.read_csv("Scopus_articles_result_author.csv", encoding='utf-8')
# convert_links(df_news)
# print(df.columns[1])
for ind in df.index:
    ab = AbstractRetrieval(df['eid'][ind], view='FULL')

    dict = {}
    dict["EID"] = ab.eid
    dict["Abstract"] = ab.abstract
    list.append(dict)

pd.DataFrame(list).to_csv("Scopus_abstract_author.csv")