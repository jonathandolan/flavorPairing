from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.generic import ListView, DetailView, CreateView
from flavorPairing.models import Ingredient, Pairing
from django import forms
from django.db.models import Q


# Views
class IngredientListView(ListView):
    model = Ingredient

    def get_queryset(self):
        qs = Ingredient.objects.all()
        return qs

class PairListView(ListView):
    model = Pairing

    def get_queryset(self, ing1):
        qs = Pairing.objects.all()
        #qs = Pairing.objects.filter(Q(ingredient1=ing1)|Q(ingredient2=ing1))
        return qs

class SearchPair(forms.Form):
    searchIngredient = forms.CharField(label="Find Pairings For:")

def find_pairings(request):
    #If post, search & return list
    t = False
    if request.method == 'POST':

        searchIngredient = request.POST.get('searchIngredient', '')

        pList = PairListView.as_view()
        t = True

    # if a GET (or any other method) we'll create a blank search form
    else:
        pList = SearchPair()

    return render(request, 'find_pair.html', {'form': pList, 'disp': t})

class PairForm(forms.Form):
    ingredient1 = forms.CharField(label='First Ingredient', max_length=30)
    ingredient2 = forms.CharField(label='Second Ingredient', max_length=30)
    pairStrength = forms.IntegerField(label='Strength of Pair')

def get_pair(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PairForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            pair1 = request.POST.get('ingredient1', '')
            pair2 = request.POST.get('ingredient2', '')
            strength = request.POST.get('pairStrength', '')
            newPair = Pairing()
            newPair.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/pair/add/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = PairForm()

    return render(request, 'add_pair.html', {'form': form})

CUISINE_CHOICES = (
        ('none', 'None'),
        ('asian', 'Asian'),
        ('european', 'European'),
        ('oceanian', 'Oceanian'),
        ('american', 'American'),
    )

class IngredientForm(forms.Form):
    ing_name = forms.CharField(label='Ingredient Name', max_length=30)
    ing_desc = forms.CharField(label='Ingredient Description', max_length=100)
    cuisine = forms.ChoiceField(label='Type of Cuisine', choices=CUISINE_CHOICES)

def get_ing_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IngredientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            newIngredientName = request.POST.get('ing_name', '')
            newIng = Ingredient(ingredientName=newIngredientName)
            newIng.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/ingredient/add/')


    # if a GET (or any other method) we'll create a blank form
    else:
        form = IngredientForm()

    return render(request, 'ingredient_form.html', {'form': form})

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',
                            {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

