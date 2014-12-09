from django.db import models
from django.core.urlresolvers import reverse

#Models

class Recipe(models.Model):
    recipeName = models.CharField(max_length=45)
    recipeDesc = models.CharField(max_length=45)
    recipeInstr = models.CharField(max_length=45)


class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=45)
    ingredientDesc = models.CharField(max_length=45)
    ingredientCategory = models.CharField(max_length=45)
    ingredientAroma = models.CharField(max_length=45)


class Cuisine(models.Model):
    cuisine_ID = models.OneToOneField(Ingredient, default=1)
    cuisineName = models.CharField(max_length=45)
    cuisineDesc = models.CharField(max_length=45)
    cuisineRegion = models.CharField(max_length=45)

class Bakery(models.Model):
    bakery_ID = models.OneToOneField(Ingredient, default=1)
    bakeryType = models.CharField(max_length=45)
    bakeryGlutenFree = models.IntegerField()


class Dairy(models.Model):
    dairy_ID = models.OneToOneField(Ingredient)
    dairyType = models.CharField(max_length=45)


class Fruit(models.Model):
    fruit_ID = models.OneToOneField(Ingredient)
    fruitClass = models.CharField(max_length=45)
    fruitFamily = models.CharField(max_length=45)


class Vegatables(models.Model):
    veg_ID = models.OneToOneField(Ingredient)
    vegFamily = models.CharField(max_length=45)
    vegCategory = models.CharField(max_length=45)

class Oil(models.Model):
    oil_ID = models.OneToOneField(Ingredient)
    oilSolid = models.IntegerField()
    oiFatType = models.CharField(max_length=45)
    oilSmokePoint = models.IntegerField()


class Meat(models.Model):
    meat_ID = models.OneToOneField(Ingredient)
    meatCut = models.CharField(max_length=45)
    meatCookStyle = models.CharField(max_length=45)


class Beverage(models.Model):
    beverage_ID = models.OneToOneField(Ingredient, default=1)
    alcoholic = models.IntegerField()
    beverageAbv = models.CharField(max_length=45)
    percentage = models.IntegerField()
    rating = models.IntegerField()


class Spice(models.Model):
    spice_ID = models.OneToOneField(Ingredient)
    spiceCuisine = models.CharField(max_length=45)
    spiceGroup = models.CharField(max_length=45)


class NutsAndSeeds(models.Model):
    n_s_ID = models.OneToOneField(Ingredient)
    classification = models.CharField(max_length=45)
    shell = models.IntegerField()


class HealthRating(models.Model):
    health_ID = models.OneToOneField(Ingredient)
    diet = models.CharField(max_length=45)
    score = models.IntegerField()
    reason = models.CharField(max_length=45)


class Pairing(models.Model):
    ingredient_ID = models.ForeignKey(Ingredient)
    ingredient2_ID = models.ForeignKey(Ingredient, related_name="ingredient2")
    ingredient1 = models.CharField(max_length=45)
    ingredient2 = models.CharField(max_length=45)
    strength = models.IntegerField()
    rating = models.IntegerField()
