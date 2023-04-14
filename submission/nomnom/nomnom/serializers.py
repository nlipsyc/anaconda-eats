from nomnom.nomnom.models import Recipe, IngredientLine
from rest_framework import serializers

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ["pk", "title", "url", "ingredients", "instructions", "thumbnail", "cook_time", "prep_time", "total_time", "serving_size"]

class IngredientLineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IngredientLine
        fields = ["pk", "url", "found_in", "quantity", "ingredient"]

