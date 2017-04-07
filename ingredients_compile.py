import json
import pandas as pd

data = pd.read_json('train.json')
print type(data)
print data.head()

ingredients = {}

i=0
for row in data.iterrows():
	for ing in row[1][2]:
		try:
			ingredients[ing] += 1
			#print ingredients
			#i+=1
		except:
			ingredients[ing] = 1

ingre = []
for ing in ingredients:
	ingre.append(ing)

with open('result2.json', 'w') as fp:
    json.dump(ingre, fp)