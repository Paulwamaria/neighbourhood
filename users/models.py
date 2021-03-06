from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic =  models.ImageField(upload_to='media/profile_pics', default='media/default.jpg')
    bio = models.TextField()
    location= models.CharField(max_length = 60, blank = True)
   


    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()