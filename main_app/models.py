from django.db import models
from django.contrib.auth.models import User

class Planet(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_planet = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profiles")
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500, default="data:image/jpeg;base64,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")
    location = models.ForeignKey(Planet, default=1, on_delete=models.CASCADE)
    bio = models.TextField(max_length=300, default="bio")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    # class Meta:
    #     ordering: ['created_at']

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# #class User(AbstractUser):
#     avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
#     bio = models.TextField()
#     def __str__(self):
#         return self.user.username
# #class User(AbstractUser):


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    title = models.CharField(max_length=100)
    comment = models.TextField(max_length=750)
    def __str__(self):
        return self.title