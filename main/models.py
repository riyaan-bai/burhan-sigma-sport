import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('sportswear', 'Sportswear'),
        ('sports shoes & sandals', 'Sports Shoes & Sandals'),
        ('sports accessories', 'Sports Accessories'),
        ('sports equipment', 'Sports Equipment'),
        ('health & fitness support', 'Health & Fitness Support'),
        ('protective gear', 'Protective Gear'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    price = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name