from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Recipe(models.Model):
    recipeID = models.IntegerField(primary_key=True)
    recipeName = models.CharField(max_length=45)
    recipeDesc = models.CharField(max_length=45)
    recipeInstr = models.CharField(max_length=45)


class Ingredient(models.Model):
    ingredientID = models.IntegerField(primary_key=True)
    ingredientName = models.CharField(max_length=45)
    ingredientDesc = models.CharField(max_length=45)
    ingredientCategory = models.CharField(max_length=45)
    ingredientAroma = models.CharField(max_length=45)
    pairingID = models.ForeignKey('Pairing')
    cuisineID = models.ForeignKey('Cuisine')

    def get_absolute_url(self):
        return reverse('ingredient-detail', kwargs={'pk': self.pk})


class Bakery(models.Model):
    ingredientID = models.ForeignKey(Ingredient)
    bakeryType = models.CharField(max_length=45)
    bakeryGlutenFree = models.IntegerField()


class Dairy(models.Model):
    ingredientID = models.ForeignKey(Ingredient)
    dairyType = models.CharField(max_length=45)


class Fruit(models.Model):
    ingredientID = models.ForeignKey(Ingredient)
    fruitClass = models.CharField(max_length=45)
    fruitFamily = models.CharField(max_length=45)


class Vegatables(models.Model):
    ingredientID = models.ForeignKey(Ingredient)
    vegFamily = models.CharField(max_length=45)
    vegCategory = models.CharField(max_length=45)

class Oil(models.Model):
    ingredientID = models.ForeignKey(Ingredient)
    oilSolid = models.IntegerField()
    oiFatType = models.CharField(max_length=45)
    oilSmokePoint = models.IntegerField()


class Meat(models.Model):
    ingredientID = models.ForeignKey(Ingredient)
    meatCut = models.CharField(max_length=45)
    meatCookStyle = models.CharField(max_length=45)


class Beverage(models.Model):
    ingredientID = models.ForeignKey(Ingredient)
    alcoholic = models.IntegerField()
    beverageAbv = models.CharField(max_length=45)
    percentage = models.IntegerField()
    rating = models.IntegerField()


class Spice(models.Model):
    ingredientID = models.ForeignKey(Ingredient)
    spiceCuisine = models.CharField(max_length=45)
    spiceGroup = models.CharField(max_length=45)


class NutsAndSeeds(models.Model):
    ingredientID = models.ForeignKey(Ingredient)
    classification = models.CharField(max_length=45)
    shell = models.IntegerField()


class Cuisine(models.Model):
    cuisineID = models.IntegerField(primary_key=True)
    cuisineName = models.CharField(max_length=45)
    cuisineDesc = models.CharField(max_length=45)
    cuisineRegion = models.CharField(max_length=45)

class HealthRating(models.Model):
    ingredientID = models.ForeignKey(Ingredient)
    diet = models.CharField(max_length=45)
    score = models.IntegerField()
    reason = models.CharField(max_length=45)


class Pairing(models.Model):
    pairingID = models.IntegerField(primary_key=True)
    ingredientID = models.ForeignKey('Ingredient')
    ingredientID2 = models.ForeignKey('Ingredient', related_name="ing2")
    strength = models.IntegerField()
    rating = models.IntegerField()
