from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    # creating a profile model by extending from built-in User model in a one-to-one relationship
    # on deleting the user, also delete the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # upload_to -> where to store the uploaded image
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s Profile"

    # overriding the default save method (to resize image and then save)
    def save(self, *args, **kwargs):
        # call the parent class save() first, and then add your modifications
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
