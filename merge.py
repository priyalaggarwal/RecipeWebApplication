import pandas as pd
import json
from pprint import pprint

# data = pd.read_json('trainp.json')
# print type(data)
# print data.head()

with open('result_combined.json') as f:
     data = json.load(f)

j=0
a = {}
for i in data:
    k=0
    value = "somekey"
    for j in i:
        if(k==0):
            value=j
            k+=1
        else:
            if j in a:
                a[j].append(value)
            else:
                a[j] = []
                a[j].append(value)



with open('trainp.json', 'w') as fp:
	json.dump(a, fp)
