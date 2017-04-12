import json

with open('final_recipe.json') as f:
	ip = json.load(f)

for row in ip:
	di = {}
	if len(row['clean_ingredients']) > len(row['ingredients']):
		for ingredient in row['ingredients']:
			for cl_ingredient in row['clean_ingredients']:
				if ingredient.find(cl_ingredient) != -1:
					if (ingredient not in di) or len(cl_ingredient) > len(di[ingredient]):
						di[ingredient] = cl_ingredient
	
	li = []
	for key in di:
		li.append(di[key])

	row['clean_ingredients'] = li


with open('trial.json', 'w') as f:
	json.dump(ip, f)