from django import forms

class IngredientForm(forms.Form):
    ingredient = forms.CharField(max_length=100)