import json

with open('cook_ndtv/recipe_op.json') as f:
	ip = json.load(f)

for row in ip:
	li = []
	for ing in row['ingredients']:
		if ing != "":
			li.append(ing)
	row['ingredients'] = li


with open('result_without_empty.json', 'w') as f:
	json.dump(ip, f)