# read data from json and convert to csv, only read doi to check redundancy 

import json
import csv

# Load your JSON data

for j in range(1,12):
    filename = "response_page" + str(j) + ".json"
    with open(filename) as json_file:
        data = json.load(json_file)

        # Print the data of dictionary
        # print("\nvalue 1:", data['metadata'])
        # print("\nvalue 2:", data['hits'][0])

        for i in range(0,30) :
            type_list = data['hits'][i]['types']
            # type_list = []
            for t in type_list:
                if t == "Article":
                    print(data['hits'][i]['uid']+ ", "+data['hits'][i]['title'].replace(',', ' ')+ ", "+data['hits'][i]['identifiers']['doi']+ ", "+str(data['hits'][i]['source']['publishYear']))
                    break