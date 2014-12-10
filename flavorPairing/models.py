from django.db import models
from django.core.urlresolvers import reverse

# Models


class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=45)
    ingredientDesc = models.CharField(max_length=45)
    ingredientCategory = models.CharField(max_length=45)
    ingredientAroma = models.CharField(max_length=45)
    ingredientBeverage = models.BooleanField(default=False)
    cuisine = models.OneToOneField('Cuisine')
    #   pairing_ID = models.ForeignKey('Pairing')


class Cuisine(models.Model):
    cuisineName = models.CharField(max_length=45)
    cuisineDesc = models.CharField(max_length=45)
    cuisineRegion = models.CharField(max_length=45)


class Pairing(models.Model):
    ingredientName1 = models.CharField(max_length=45, default=" ")
    ingredientName2 = models.CharField(max_length=45, default=" ")
    ingredientRelationship1 = models.OneToOneField('Ingredient', default=0)
    ingredientRelationship2 = models.OneToOneField('Ingredient', related_name=" ", default=0)
    strength = models.IntegerField()
    rating = models.IntegerField()