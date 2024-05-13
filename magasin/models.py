from django.db import models
from datetime import date
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Categorie(models.Model):
    TYPE_CHOICES=[
        ('Al', 'Alimentaire'), 
        ('Mb', 'Meuble'),
        ('Sn', 'Sanitaire'), 
        ('Vs', 'Vaisselle'),
        ('Vt', 'Vêtement'),
        ('Jx', 'Jouets'),
        ('Lg', 'Linge de Maison'),
        ('Bj', 'Bijoux'),
        ('Dc', 'Décor')
    ]
    name = models.CharField(max_length=50, default='Alimentaire', choices=TYPE_CHOICES)    

    def __str__(self):
        return self.name

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)

    def __str__(self):
        return self.nom    

class Produit(models.Model):
    TYPE_CHOICES = [
        ('fr', 'Frais'),
        ('cs', 'Conserve'),
        ('em', 'Emballé')
    ]

    libelle = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='em')
    image = models.ImageField(upload_to='media/', default='default_image.jpg')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.libelle} - {self.description} - {self.prix}"

class ProduitNC(Produit):
    duree_garantie = models.CharField(max_length=100)
class ProduitC(Produit):
    def __str__(self):
        return f"{super().__str__()} (Consommable)"
class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today())
    produits = models.ManyToManyField('Produit')
    totalCde = models.FloatField(editable=False)

    def recalculer_total(self): 
        total = sum(produit.prix for produit in self.produits.all()) 
        self.totalCde = total
        self.save() 
    
    def listerProd(self):
        ch = ''
        for v in self.produits.all():
            ch += v.__str__()
        return ch

    def __str__(self):
        return str(self.dateCde) + " " + str(self.totalCde) + self.listerProd()

@receiver(m2m_changed, sender=Commande.produits.through)
def update_total(sender, instance, **kwargs): 
    if kwargs['action'] in ['post_add', 'post_remove', 'post_clear']: 
        instance.recalculer_total()   
