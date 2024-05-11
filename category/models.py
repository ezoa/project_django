from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name= models.CharField(max_length=80,unique=True)
    slug= models.SlugField(max_length=60,unique=True)
    description = models.CharField(max_length=255, blank=True)
    cat_image= models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural ='categories'
    
    
    #To create a link between some elements
    
    def get_url(self):
        
        return reverse('products_by_category',args=[self.slug])

    
    def __str__(self):
        return self.category_name
    

    
