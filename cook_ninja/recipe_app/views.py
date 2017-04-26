from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Recipe, Ingredient
from neomodel import db
import json
from django.views.decorators.csrf import csrf_exempt

# from dal import autocomplete

@csrf_exempt
def index(request):
    # template_name = 'recipe_app/index.html'
    # context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')[:5]
    # model = Recipe

    # recipe = Recipe.objects.filter(name='Cucumber Soup')[0]
    

    # get ingredients from recipe
    # recipe = Recipe.nodes.get(name='Cucumber Soup')
    # print recipe
    # print "--associated ingredients--"
    # print recipe.ingredient.all()

    # print '---------------------------'
    # # get recipe from ingredients
    # ingredient_list = ["fennel","sugar","mustard oil"]
    # ingredient = Ingredient.nodes.filter(name__in=ingredient_list)

    # print "--associated recipes--"
    # # for r in ingredient.recipe.all():
    # #     print r.name

    

    # # print '-----------'
    # ingredient_list = ["fennel","sugar","mustard oil"]

    # query = """ match(r:Recipe)-[:CHILD]->(i:Ingredient)
    #         where i.name in {ingredient_list}
    #         with r,count(*) as c
    #         where c > 1
    #         return *
    #         order by c desc
    #         limit 5"""

    # results, meta = db.cypher_query(query, params={"ingredient_list":ingredient_list})
    # # print len(results[0])
    # for r in results:
    #     print r[0] # no of ingredients that matched
    #     print r[1].properties['name']
    #     print r[1].properties['ingredients']
    #     print r[1].properties['description']
    #     # more properties to be added here
    # if len(request.session.get('ingredient_list')) != 0:
    #     return redirect(reverse('recipe_app:recipe_listing'))
    # if request.is_ajax():
    #     ingredient_list = request.POST.getlist('ingredients[]')
    #     return redirect(reverse('recipe_app:recipe_listing'))
    # li = []
    # request.session.ingredient_list = li
    request.session['ingredient_list'] = []
    return render(request, 'recipe_app/index.html')


def get_ingredients(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        query = 'match(i:Ingredient) where i.name contains {q} return(i) order by length(i.name) limit 10;'
        ingredients, meta = db.cypher_query(query, params={"q":q})
        # ingredients = sorted(Ingredient.nodes.filter(name__icontains = q)[:10], key=lambda o:len(o.name))
        # print ingredients
        results = []
        id = 0
        for ingredient in ingredients:
            ingredient_json = {}
            ingredient_json['id'] = id
            id += 1
            ingredient_json['label'] = ingredient[0].properties['name']
            ingredient_json['value'] = ingredient[0].properties['name']
            results.append(ingredient_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'

    return HttpResponse(data, mimetype)

@csrf_exempt
def selected_ingredients(request):
    ingredient_list = request.POST.getlist('ingredients[]')
    # print ingredient_list
    request.session['ingredient_list'] = ingredient_list
    # print request.session['ingredient_list']
    # response = {'status': 1, 'message': _("Ok")}
    # return HttpResponse(json.dumps(response), content_type='application/json')
    # return redirect(reverse('recipe_app:recipe_listing'))
    return HttpResponse('success')

def recipe_detail(request, id):
    recipe = Recipe.nodes.filter(index=id)[0]
    # print recipe.cook_time
    # print recipe
    return render(request, 'recipe_app/recipe_detail.html', {"recipe" : recipe})

def recipe_listing(request):
    # ingredient_list = ["fennel","sugar","mu    stard oil"]
    ingredient_list = request.session.get('ingredient_list')
    print ingredient_list
    # query = """ match(r:Recipe)-[:CHILD]->(i:Ingredient)
    #         where i.name in {ingredient_list}
    #         with r,count(*) as c
    #         where c > 1
    #         return *
    #         order by c desc
    #         limit 5"""
    
    query = """ match(r:Recipe)-[:CHILD]->(i:Ingredient)
        where i.name in {ingredient_list}
        RETURN count(*) as degree,r as recipe
        ORDER BY degree DESC
        LIMIT 3"""

    results, meta = db.cypher_query(query, params={"ingredient_list":ingredient_list})
    # print len(results[0])
    recipes = []

    for r in results:
        recipes.append({'no_matched' : r[0], 'name' : r[1].properties['name'],
            'image_path' : r[1].properties['image_path'] , 'id' : r[1].properties['index'],
            'description' : r[1].properties['description']})

    print recipes
    return render(request, 'recipe_app/recipe_listing.html', {"recipes" : recipes })
    # return HttpResponse('success')
    
def categoryresult(request, name):
    recipes = Recipe.nodes.filter(category = name)[:10]
    return render(request, 'recipe_app/categoryresult.html', {"recipes" : recipes, "category_name" : name })

def all_categories(request):
	return render(request, 'recipe_app/category.html')
