# RecipeWebApplication

### final_recipe.json
Final recipe data with clean ingredients and index

### json_modify.py
Script to create 'clean ingridients' field in the json. Outputs the final data i.e final_recipe.json

### merge.py
Pranav's intermediate script for final_recipe.

### recipe_empty_clean.json
The field clean ingredients having empty list is created. Used for an intermediate step in json_modify.py. Ignore this file.

### remove_empty_ingredients.py
Removes the blank ingredients from original data. Basically, recipe_op.json is modified. recipe_op_uncleaned.json is the previous file with blank ingredients.

### result_combined.json
Only modified the formatting (Pretty Print JSON)

### add_list_cl_ing_field.py
Script to add clean list field in the json before pandas processing.

### extra_ingridients_remover.py
Script to remove redundant ingredients from clean list

### final_recipe_extra.json
final_recipe data before removing redunadant ingredients

### remove_empty_ingredients.py
Removes the the empty ingredient fields from the original json file.
