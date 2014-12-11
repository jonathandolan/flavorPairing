from django.db import models
from django.core.urlresolvers import reverse

# Models


class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=45)
    ingredientDesc = models.CharField(max_length=45)
    ingredientCategory = models.CharField(max_length=45)
    ingredientAroma = models.CharField(max_length=45)
    ingredientBeverage = models.BooleanField(default=False)
    CUISINE_CHOICES = (
        ('none', 'None'),
        ('asian', 'Asian'),
        ('european', 'European'),
        ('oceanian', 'Oceanian'),
        ('american', 'American'),
    )
    cuisine = models.CharField(max_length=8,choices=CUISINE_CHOICES, default='none')

    def __str__(self):
        return self.ingredientName


class Cuisine(models.Model):
    cuisineName = models.CharField(max_length=45)
    cuisineDesc = models.CharField(max_length=45)
    cuisineRegion = models.CharField(max_length=45)


class Pairing(models.Model):
    ingredientName1 = models.CharField(max_length=45, default=" ")
    ingredientName2 = models.CharField(max_length=45, default=" ")
    ingredientRelationship1 = models.OneToOneField('Ingredient', default=1)
    ingredientRelationship2 = models.OneToOneField('Ingredient', related_name=" ", default=1)
    strength = models.IntegerField()

