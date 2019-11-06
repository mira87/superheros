from django.db import models

# Create your models here.
class SuperHero(models.Model):
    superhero_name=models.CharField(max_length=200,null=True)
    real_name=models.CharField(max_length=200)
    publisher=models.CharField(max_length=400, null=True)
    photo_url=models.TextField()
    occupation=models.TextField(null=True, blank=True)
    place_of_birth=models.TextField(null=True, blank=True)
    first_appear=models.TextField(null=True, blank=True)
    group_affiliation=models.TextField(null=True, blank=True)
    relatives=models.TextField(null=True, blank=True)
    superpowers=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.real_name
        
