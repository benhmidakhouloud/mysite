from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView
# Create your models here.
STATUS = (
(0,"Draft"),
(1,"Publish")
)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image=models.ImageField(blank=True)
    class Meta:
        ordering = ['-created_on']
    def __str__(self):
        return self.title
class MonObjetListView(ListView): 
    model = Post # Spécifie le modèle associé à cette vue 
    template_name = 'blog/list.html'
    # Chemin vers le template utilisé pour afficher le formulaire de modification 
    context_object_name = 'posts' # Nom de l'objet de contexte dans le template 
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.author} on '{self.post}'" 
