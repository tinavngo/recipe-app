from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length= 120)
    ingredients = models.CharField(max_length= 200, help_text="Enter the ingredient, separated by comma")
    cooking_time = models.PositiveIntegerField( help_text='Enter time in minutes')

    def __str__(self):
        return f"-- Recipe: {self.name} -- Ingredients: {self.ingredients} // Cooking Time: {self.cooking_time} minutes "
