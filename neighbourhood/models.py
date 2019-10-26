from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=60)
    neighborhood_location = models.CharField(max_length=60)
    image = models.ImageField(upload_to='media/hood/', blank = True, null =True)
    occupants = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.neighborhood_name


    def save_neighborhood(self):
        self.save()

    @classmethod
    def delete_neighborhood(cls,neighborhood):
        cls.objects.filter(neighborhood=neighborhood).delete()




class Business(models.Model):
    business_name = models.CharField(max_length=60)
    description = models.TextField()
    neighborhood = models.ForeignKey(Neighborhood, related_name='businesses',  on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='media/business/', blank = True, null =True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_email = models.EmailField()


    def __str__(self):
        return self.business_name


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()



class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    neighborhood = models.ForeignKey(Neighborhood, related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/blog/', blank = True, null =True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return self.title


    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()