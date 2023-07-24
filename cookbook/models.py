from django.conf import settings
from django.db import models


class BaseRecipe(models.Model):
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        abstract = True


class Recipe(BaseRecipe):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    cooking_time = models.IntegerField()
    ingredients = models.ManyToManyField("Ingredient", through='IngredientRecipe')
    published_date = models.DateTimeField()


class Instruction(BaseRecipe):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class IngredientRecipe(models.Model):
    class MeasuringUnit(models.TextChoices):
        milligram = 'mg'
        gram = 'g'
        kg = 'kg'
        milliliter = 'ml'
        liter = 'l'

    weight = models.FloatField()
    measuring_unit = models.CharField(max_length=10, choices=MeasuringUnit.choices, default=MeasuringUnit.gram)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)


class Ingredient(models.Model):
    title = models.CharField(max_length=300)
    calories = models.FloatField()
    fat = models.FloatField(null=True, blank=True)
    saturates = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
