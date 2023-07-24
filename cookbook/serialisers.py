from rest_framework import serializers

from .models import Recipe, Category, IngredientRecipe, Ingredient, Instruction


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class IngredientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Recipe
        fields = '__all__'


class InstructionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = '__all__'


class IngredientRecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = IngredientRecipe
        fields = '__all__'
