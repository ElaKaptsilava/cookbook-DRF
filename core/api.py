from rest_framework import routers
from cookbook import views as cookbookViews

router = routers.DefaultRouter()
router.register(r'recipes', cookbookViews.RecipeViewSet, basename='recipe')
router.register(r'category', cookbookViews.CategoryViewSet, basename='category')
router.register(r'ingredient-recipe', cookbookViews.IngredientRecipeViewSet, basename='ingredient-recipe')
router.register(r'ingredient', cookbookViews.IngredientViewSet, basename='ingredient')
router.register(r'instruction', cookbookViews.InstructionViewSet, basename='instruction')
