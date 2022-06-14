from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    bio=models.TextField()
    image=models.ImageField(upload_to='profiles/',null=True)

    # save,delete,update,search methods
    def __str__(self):
        return self.user.username

class Project(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='screenshots/',null=True)
    description=models.TextField()
    url=models.URLField(max_length=50)

    # save,delete,update,search methods
    def __str__(self):
        return self.title