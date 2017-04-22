# from neo4django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty, ArrayProperty, RelationshipFrom, RelationshipTo
# Create your models here.

class Recipe(StructuredNode):
	name = StringProperty()
	index = IntegerProperty()
	method = ArrayProperty()
	image_path = StringProperty()
	image_url = StringProperty()
	description = StringProperty()
	category = StringProperty()
	ingredients = ArrayProperty()
	cook_time = StringProperty()
	tags = ArrayProperty()
	
	ingredient = RelationshipTo('Ingredient','CHILD')

class Ingredient(StructuredNode):
	name = StringProperty()

	recipe = RelationshipFrom('Recipe','CHILD')


# class Ingredient(models.NodeModel):
# 	name = StringProperty()