from nomnom.nomnom.models import Recipe, IngredientLine
from rest_framework import viewsets
from rest_framework import permissions
from nomnom.nomnom.serializers import RecipeSerializer, IngredientLineSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """
    queryset = Recipe.objects.all().order_by('-created')
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]


class IngredientLineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = IngredientLine.objects.all().order_by('-recipe')
    serializer_class = IngredientLineSerializer
    permission_classes = [permissions.AllowAny]