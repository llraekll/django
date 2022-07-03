from this import d 
from django.urls import reverse
from django.db import models

class Product(models.Model):
    title= models.CharField(max_length=120)
    description= models.TextField(blank=True, null=True)
    price= models.DecimalField(decimal_places=2, max_digits=1000)
    summary= models.TextField(blank=False, null=False)
    featured= models.BooleanField(default=True)

#    def get_absolute_url(self):
 #           return reverse("product-detail", kwargs={'id': self.id})    #f"/products/{self.id}/"
    def get_absolute_url(self):
       return reverse("product-detail", kwargs={'id': self.id}) #f"/products/{{instance.id}}/"