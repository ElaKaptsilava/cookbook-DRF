from rest_framework import viewsets

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Recipe, Category, IngredientRecipe, Ingredient, Instruction
from .serializers import RecipeSerializers, CategorySerializers, IngredientRecipeSerializers, IngredientSerializers, \
    InstructionSerializers


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
    permission_classes = [IsOwnerOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [IsAdminOrReadOnly]


class IngredientRecipeViewSet(viewsets.ModelViewSet):
    queryset = IngredientRecipe.objects.all()
    serializer_class = IngredientRecipeSerializers
    permission_classes = [IsOwnerOrReadOnly]


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers
    permission_classes = [IsAdminOrReadOnly]


class InstructionViewSet(viewsets.ModelViewSet):
    queryset = Instruction.objects.all()
    serializer_class = InstructionSerializers
    permission_classes = [IsOwnerOrReadOnly]
