
from django.shortcuts import render
from inventory.models import SeasonalFlavor, Ingredient, CustomerSuggestion

# View to display all seasonal flavors
def seasonal_flavor_list(request):
    flavors = SeasonalFlavor.objects.all()
    return render(request, 'inventory/seasonal_flavor_list.html', {'flavors': flavors})

# View to display all ingredients
def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'inventory/ingredient_list.html', {'ingredients': ingredients})

# View to display all customer suggestions
def customer_suggestion_list(request):
    suggestions = CustomerSuggestion.objects.all()
    return render(request, 'inventory/customer_suggestion_list.html', {'suggestions': suggestions})