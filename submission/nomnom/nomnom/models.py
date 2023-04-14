from django.db import models

class IngredientLine(models.Model):
    found_in = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=32)
    quantity = models.SmallIntegerField()


class Recipe(models.Model):
    title = models.CharField(max_length=64)
    ingredients = models.ManyToManyField("IngredientLine", blank=True)
    instructions = models.TextField()
    thumbnail = models.URLField()
    cook_time = models.DurationField()
    prep_time = models.DurationField()
    total_time = models.DurationField()
    serving_size = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    