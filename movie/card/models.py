from django.db import models

# Create your models here.

class Cards(models.Model):
    title=models.CharField(max_length=20)
    desc=models.CharField(max_length=500)
    year=models.IntegerField()
    image=models.ImageField(upload_to="card/image",null=True,blank=True)

    def __str__(self):
        return self.title