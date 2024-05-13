from django.shortcuts import render, HttpResponseRedirect
from .forms import ProduitForm,FournisseurForm,CommandeForm
from .models import Produit, Fournisseur, Commande
from .forms import ProduitForm, FournisseurForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie,Produit
from magasin.serializers import CategorySerializer,ProduitSerializer
from rest_framework import viewsets

def index(request):
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html', context)

def form(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('magasin/')
    else:
        form = ProduitForm()  # create empty form
    return render(request, 'magasin/majProduits.html', {'form': form})


def vitrine(request):
    list=Produit.objects.all()
    return render(request,'magasin/vitrine/vitrine.html',{'list':list})




def formFournisseur(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = FournisseurForm()  # create empty form
    return render(request, 'magasin/fournisseur.html', {'form': form})
def nouvelleCommande(request):
    if request.method == "POST" :
        form=CommandeForm(request.POST,request.FILES)  
        
        if form.is_valid():
            cde=form.save()
            #return redirect('/magasin')
    else:
        form=CommandeForm() #créer formulaire vide
        cde=form
        
    liste=Commande.objects.all()
    context={'form':form,'lesCdes':liste,'cd':cde}
    return render(request,'magasin/nouvelleCommande.html',context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bonjour {username}, votre compte a été créé avec succès !')
                return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class ProduitAPIView(APIView):
    def get(self, request, format=None):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

    