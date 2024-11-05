
from django.db import models

class SeasonalFlavor(models.Model):
    SEASON_CHOICES = [
        ('Winter', 'Winter'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall', 'Fall'),
    ]
    flavor_name = models.CharField(max_length=100)
    description = models.TextField()
    season = models.CharField(max_length=10, choices=SEASON_CHOICES)

    def _str_(self):
        return f"{self.flavor_name} ({self.season})"


class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilograms'),
        ('g', 'Grams'),
        ('lbs', 'Pounds'),
        ('oz', 'Ounces'),
        ('liters', 'Liters'),
        ('ml', 'Milliliters'),
    ]
    ingredient_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)

    def _str_(self):
        return f"{self.ingredient_name} - {self.quantity} {self.unit}"


class CustomerSuggestion(models.Model):
    customer_name = models.CharField(max_length=100)
    flavor_suggestion = models.CharField(max_length=100, blank=True, null=True)
    allergy_concern = models.TextField(blank=True, null=True)

    def _str_(self):
        return f"Suggestion by {self.customer_name}"