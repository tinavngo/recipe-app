from django.test import TestCase
from .models import Recipe

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