import json

with open('cook_ndtv/recipe_op.json') as f:
	ip = json.load(f)

for row in ip:
	row['clean_ingredients'] = []

with open('trial.json', 'w') as f:
	json.dump(ip, f)