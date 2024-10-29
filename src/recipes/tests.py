from django.test import TestCase
from .models import Recipe
from django.urls import reverse

# Create your tests here.
class RecipeModelTest(TestCase):

    def setUpTestData():
        # set up recipe object for testing
        Recipe.objects.create(name='Tea', ingredients='Sugar, Water, Tea Leaves', cooking_time='3')

    def test_recipe_name(self):
        # fetch recipe object by id
        recipe = Recipe.objects.get(id=1)
        # get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('name').verbose_name
        # compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_ingredient_max_length(self):
        # fetch recipe object by id
        recipe = Recipe.objects.get(id=1)
        # get the metadata for the 'ingredients' field and use it to query its data
        max_length = recipe._meta.get_field('ingredients').max_length
        # compare the value to the expected result
        self.assertEqual(max_length, 200)

    def test_cooking_time_integer(self):
        # fetch recipe object by id
        recipe = Recipe.objects.get(id=1)
        # checks if the object is an integer
        self.assertIsInstance(recipe.cooking_time, int)
        # checks if the object is greater than 0
        self.assertGreater(recipe.cooking_time, 0)

    def test_string_representation(self):
        # Test the string representation of a Recipe object (should be its name).
        self.assertEqual(str(self.recipe), self.recipe.name)
    
    def test_return_ingredients_as_list(self):
        # Ensure the ingredients are correctly split into a list.
        ingredients_list = self.recipe.return_ingredients_as_list()
        self.assertEqual(len(ingredients_list), 3)
    
    def test_calculate_difficulty(self):
        # Test the difficulty calculation for various scenarios.
        self.recipe.cooking_time = 5
        self.recipe.ingredients = 'Ingredient1,Ingredient2'
        self.recipe.save()
        self.assertEqual(self.recipe.difficulty, 'Easy')
        
        self.recipe.cooking_time = 15
        self.recipe.ingredients = 'Ingredient1,Ingredient2,Ingredient3,Ingredient4'
        self.recipe.save()
        self.assertEqual(self.recipe.difficulty, 'Hard')
        
    def test_save_method_override(self):
        # Check that the difficulty is correctly set when a Recipe is saved.
        self.recipe.cooking_time = 20
        self.recipe.ingredients = 'Ingredient1,Ingredient2,Ingredient3'
        self.recipe.save()
        self.assertEqual(self.recipe.difficulty, 'Intermediate')
    
    def test_default_image_path(self):
        # Verify the default image path is set as expected.
        self.assertEqual(self.recipe.pic, 'no_picture')

class RecipeViewsTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Set up data for the view tests.
        cls.recipe = Recipe.objects.create(
            name='View Test Recipe',
            ingredients='Ingredient1,Ingredient2,Ingredient3',
            cooking_time=20,
            difficulty='Medium',
            description='View Test Description'
        )
    
    def test_home_page_status_code(self):
        # Test the home page is accessible and returns a HTTP 200 status.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_list_view(self):
        # Verify the recipe list view works and includes the recipe's name.
        response = self.client.get(reverse('recipes:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test Recipe')
    
    def test_recipe_detail_view(self):
        # Test the recipe detail view displays the correct recipe details.
        response = self.client.get(reverse('recipes:detail', args=[self.recipe.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Test Recipe')
    
    def test_recipe_detail_view_with_nonexistent_recipe(self):
        # Check that a non-existent recipe detail view returns a 404 status.
        response = self.client.get(reverse('recipes:detail', args=[999]))
        self.assertEqual(response.status_code, 404)