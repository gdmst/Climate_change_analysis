import pybliometrics
# Document-specific information
# from pybliometrics.scopus import AbstractRetrieval
from pybliometrics.scopus import ScopusSearch
import pandas as pd

pybliometrics.scopus.init()

#1. search for articles by keywords
q = 'AUTHKEY(health* OR COVID OR medic* OR treatment OR clinic OR therapy OR vaccin* OR smoking OR tobacco OR cigarette OR pandemic OR coronavirus OR autism OR mmr OR zika OR immunization OR cancer OR pregnancy OR HIV OR AIDS OR prep OR STD OR HPV OR contraception OR condom OR dental OR oral OR nutrition OR diet OR vitamin OR disease OR patient OR physician OR doctor OR nurse OR psychiatrist OR medication OR antibiotics OR diabetes OR ebola OR H1N1 OR epidemics OR measles OR vaping OR Influenza OR Respiratory OR "Nile virus" OR Gynaecologic OR Fluoride OR fluoridation OR heart OR hypertension OR Inflammatory OR Psoriasis OR Anorexia OR Abortion OR Dialysis OR Drug OR Sclerosis OR Paediatric OR Tonsillectomy OR Suicide OR SARS OR Dengue OR poliomyelitis OR neurological OR gastrointestinal OR cardiovascular OR urological OR disorders OR MERS OR H7N9 OR Eating OR proana OR diphtheria OR prostate OR epilepsy) AND AUTHKEY(misinformation OR disinformation OR "fake news")'
q = q + ' AND PUBYEAR < 2025'
s = ScopusSearch(q, subscriber=False)
print("search for articles")
# print(s)

# 2. save data to csv
df = pd.DataFrame(s.results)

filtered_df = df[df["subtype"] == "ar"]

filtered_df.to_csv("Scopus_articles_health_result_2.csv")

