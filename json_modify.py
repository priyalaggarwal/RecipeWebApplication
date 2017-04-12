import pandas as pd
import json
from math import isnan


data = pd.read_json('result_combined.json')

recipes = pd.read_json('recipe_empty_clean.json')
	
for row in data.iterrows():
	i = 1
	while(i < 2670 and isnan(row[1][i]) == False):
		recipes['clean_ingredients'][row[1][i]].append(row[1][0])
		i += 1

recipes.reset_index().to_json('final_recipe.json', orient="records")