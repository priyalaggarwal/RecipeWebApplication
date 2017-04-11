import pandas as pd
import json

data = pd.read_json('result2.json')
#print type(data)
#print data.head()

recipes = pd.read_json('cook_ndtv/recipe_op.json')
#print recipes.shape
ingredient_cols = recipes['ingredients']
# print ingredient_cols
fin_arr = []
left_out = []
j=0
for col in ingredient_cols:
	temp = []
	for i in col:
		temp.append(0)
	left_out.append(temp)

for row in data.iterrows():
	ing = row[1][0]
	# print ing
	temp_arr = []
	temp_arr.append(ing)
	j=0
	for col in ingredient_cols:
		for i in col:
			i = i.lower()
			if i.find(ing) != -1:
				temp_arr.append(j)
				break
		k = 0
		for i in col:
			i = i.lower()
			if i.find(ing) != -1:
				left_out[j][k]+=1;
				#print ingredient_cols[j][k]
			k+=1
		j+=1
	if len(temp_arr)!=1:
		fin_arr.append(temp_arr)

#print len(fin_arr)
#print left_out
count = 0
total = 0
k=0
l=0
for i in left_out:
	l=0
	for j in i:
		if left_out[k][l]==0:
			print ingredient_cols[k][l]
			print k
		l+=1
	k+=1
	count += i.count(0)
	total += len(i)
print count
print total
with open('result_combined.json', 'w') as fp:
	json.dump(fin_arr, fp)