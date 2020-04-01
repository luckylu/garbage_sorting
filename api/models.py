from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30)

class Garbage(models.Model):
    name = models.CharField(max_length = 30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + str(self.category)

