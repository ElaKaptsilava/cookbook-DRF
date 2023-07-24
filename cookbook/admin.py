from django.contrib import admin
from .models import Recipe, Instruction, Ingredient, IngredientRecipe, Category

admin.site.site_header = "CookBook Django"


class InstructionsInline(admin.TabularInline):
    model = Instruction
    extra = 1


class IngredientsInLine(admin.TabularInline):
    model = IngredientRecipe
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [InstructionsInline, IngredientsInLine]
    list_display = ["user", "category", "title", "published_date"]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(IngredientRecipe)
