from django.db import models
from django.contrib.auth.models import User


class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=60)
    neighborhood_location = models.CharField(max_length=60)
    image = models.ImageField(upload_to='media/hood/', blank = True, null =True)
    occupants = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.neighborhood_name


    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()