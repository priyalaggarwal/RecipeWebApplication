import json
import pandas as pd

recipes = pd.read_json('cook_ndtv/recipe_op.json')
category_col = recipes['category']

#print category_col[0]

categories = {}

i=0
for row in category_col:
		try:
			categories[row] += 1
		except:
			categories[row] = 1

categ = []
for cat in categories:
	categ.append(cat)

with open('categories.json', 'w') as fp:
    json.dump(categ, fp)
