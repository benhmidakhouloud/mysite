from django.urls import path,include
from . import views
from .views import ListePost , DetailPost , CreerPost , ModifierPost , SupprimerPost
urlpatterns = [
path('', ListePost.as_view() , name='liste_posts'),
path('<int:pk>/', DetailPost.as_view(), name='detail_post'),
path('creer_post/', CreerPost.as_view() , name='creer_post'),
path('<int:pk>/modifier_post/', ModifierPost.as_view() , name='modifier_post'),
path('<int:pk>/supprimer_post/', SupprimerPost.as_view() , name='supprimer_post')
]