from django.conf.urls import url

from . import views

app_name = 'recipe_app'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^api/get_ingredients/', views.get_ingredients, name='get_ingredients'),
	url(r'^selected_ingredients/', views.selected_ingredients, name='selected_ingredients'),
	url(r'^recipe_detail/(?P<id>[0-9]+)/', views.recipe_detail, name='recipe_detail'),
	url(r'^recipe_listing/', views.recipe_listing, name='recipe_listing'),
	# the name attribute is referred in templates {% url %}
	# url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
 #    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
 #    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
