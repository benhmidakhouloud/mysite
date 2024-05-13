from django.urls import path,include
from . import views
from .views import CategoryAPIView
from .views import ProduitAPIView
urlpatterns = [
    path('', views.index, name='index'),
    path('majProduit/', views.form, name='majProduit'),
    path('vitrine/', views.vitrine, name='vitrine'),
    path('nouveauFournisseur/', views.formFournisseur, name='nouveau_fournisseur'),
    path('nouvelleCommande/', views.nouvelleCommande, name='nouvelle_commande'),
    path('register/',views.register, name = 'register'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view(), name='produits_api'),
    
]
