from django.urls import path
from .views import home, RecipeListView, RecipeDetailView
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path("list/", RecipeListView.as_view(), name="list"),
    path("list/<int:pk>/", RecipeDetailView.as_view(), name="detail"),
    path('recipes/search/', views.RecipeSearchView.as_view(), name='recipe_search'),
]
