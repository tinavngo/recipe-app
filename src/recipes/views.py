from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'recipes/recipes_home.html')

# View for recipe lists, login required
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"

# View for recipe lists, login required
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name= "recipes/recipe_details.html"

# View for recipe lists, login required
class RecipeSearchView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipe_search.html'
    def get_queryset(self):
        query = self.request.GET.get('recipes')
        if query:
            return Recipe.objects.filter(name__icontains=query)
        return Recipe.objects.all()