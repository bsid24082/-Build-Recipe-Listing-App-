from django.shortcuts import render
from .models import *
from labexam.settings import BASE_DIR


# Create your views here.

def index(request):
    # cars_data.objects.all().delete() #To Delete the data
    reciped = recipes.objects.all()
    return render(request, 'index.html', {'recipes':reciped, 'BASE_DIR':BASE_DIR})


def admin1(request):
    if request.method == 'POST':
        recipe = recipes()
        recipe.name = request.POST.get("name", False)
        recipe.description = request.POST.get("description", False)
        recipe.ingredients = request.POST.get("ingredients", False)
        recipe.image = request.FILES.get("image", False)
        recipe.save()

    
    return render(request, 'upload.html')