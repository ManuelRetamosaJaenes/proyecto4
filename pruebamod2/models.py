from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table="publicacion"
        verbose_name='Publicacion'
        ordering=['title']


class Article2(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
    
    class Meta:
        db_table="articulo2"
        verbose_name='Articulo2'
        ordering = ["headline"]