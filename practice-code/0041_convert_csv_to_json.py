# pip install pandas

import json
import pandas as pd

# read data from csv data file
csv_data = pd.read_csv('data.csv')
print(csv_data)

# convert csv data to json data
json_data = json.dumps(list(csv_data.reader(open('data.csv'))))
print(json_data)