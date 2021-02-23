from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=254)
    department = models.CharField(max_length=500)
    roll_no = models.CharField(max_length=50)
    message = models.TextField()

    class Meta:
        app_label = 'contact'

    def __str__(self):
        return self.name
    