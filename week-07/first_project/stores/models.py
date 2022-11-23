from django.db import models
from django.db.models import CASCADE


class Store(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(help_text='the link to store URL (external)')
    description = models.TextField(null=True, blank=True)
    email = models.EmailField(verbose_name='Email Address')

    def __str__(self):
        return self.name


class Product(models.Model):
    store = models.ForeignKey(to=Store, on_delete=CASCADE, related_name='products')
    name = models.CharField(max_length=300)
    price = models.PositiveIntegerField(default=900)
    is_available = models.BooleanField(default=False)
    pdf = models.FileField(upload_to='product-files/', null=True, blank=True)

    def __str__(self):
        return f'{self.name} -- ${self.price}'
