import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('fitness equipment', 'Fitness Equipment'),
        ('socks', 'Socks'),
        ('ball', 'Ball'),
        ('shoes', 'Shoes'),
        ('accessories', 'Accessories'),
        ('clothes', 'Clothes'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    price = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()