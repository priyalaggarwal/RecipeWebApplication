# tutorial link http://www.markhneedham.com/blog/2015/07/23/neo4j-loading-json-documents-with-cypher/

import json
from py2neo import Graph, authenticate
 
authenticate("localhost:7474", "neo4j", "webtech@123")
graph = Graph()
 
with open('final_recipe.json') as data_file:
    json = json.load(data_file)
 
# query = """
# WITH {json} AS document
# UNWIND document.recipies AS recipe
# RETURN recipe.name
# """


# query = """
# WITH {json} AS document
# UNWIND document.recipies AS recipe
# UNWIND recipe.ingredients AS ingredient
# RETURN recipe.name, ingredient
# """

# query that needs to be executed in neo4j
query = """
WITH {json} AS document
UNWIND document.recipies AS recipe
UNWIND recipe.images AS image
UNWIND recipe.clean_ingredients AS ingredient

MERGE (r:Recipe {name: recipe.name, category: recipe.category, 
description: recipe.description, cook_time : recipe.cook_time, 
prep_time : recipe.prep_time, ingredients: recipe.ingredients, 
method : recipe.method, tags : recipe.tags, image_path: image.path, 
image_url : recipe.image_urls, index: recipe.index})
MERGE (i:Ingredient {name: ingredient})
MERGE (r)-[:CHILD]->(i)
"""
# ingredients: recipe.ingredients, method : recipe.method, tags : recipe.tags, images: recipe.images,  image_urls : recipe.image_urls

# 

# Send Cypher query.
print graph.run(query, json = json).dump()

## query to run in neo4j server to display final result
# match (recipe:Recipe)-[:CHILD]->(ingredient)
# return *