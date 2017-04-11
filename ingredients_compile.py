import json
import pandas as pd

data = pd.read_json('train.json')
data2 = open('ingredient_list_ndtv.txt','r')

print type(data)
print data.head()

ingredients = {}

i=0
for row in data.iterrows():
	for ing in row[1][2]:
		try:
			ing = ing.lower()
			ingredients[ing] += 1
			#print ingredients
			#i+=1
		except:
			ingredients[ing] = 1

for line in data2:
	try:
		line=line.lower().strip()
		ingredients[line] += 1
	except:
		ingredients[line] = 1

# add common ingredients which were still not available
try:
	ingredients["potato"] +=1
	ingredients["chilli"] +=1
	ingredients["prawn"] +=1
	ingredients["curd"] +=1
	ingredients["green chilly"] +=1
	ingredients["maida"] +=1
	ingredients["besan"] +=1
	ingredients["saunf"] +=1
	ingredients["almond"] +=1
	ingredients["cashew"] +=1
	ingredients["hing"] +=1
	ingredients["zeera"] +=1
	ingredients["brinjal"] +=1
	ingredients["apple"] +=1
except:
	ingredients["potato"] = 1
	ingredients["chilli"] =1
	ingredients["prawn"] =1
	ingredients["curd"] =1
	ingredients["green chilly"] =1
	ingredients["maida"] =1
	ingredients["besan"] =1
	ingredients["saunf"] =1
	ingredients["almond"] =1
	ingredients["cashew"] =1
	ingredients["hing"] =1
	ingredients["zeera"] =1
	ingredients["brinjal"] =1
	ingredients["apple"] =1

ingre = []
for ing in ingredients:
	ingre.append(ing)

with open('result2.json', 'w') as fp:
    json.dump(ingre, fp)