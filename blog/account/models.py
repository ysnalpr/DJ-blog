import os
from django.db import models
from django.conf import settings


def change_image_name(instance, filename):  # To change the image name
    ext = filename.split(".")[-1]
    filename = "%s_%s.%s" % (instance.user.id, instance.user.username, ext)
    return os.path.join("users", filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=change_image_name, blank=True)
    date_of_birth = models.DateField(
        blank=True, null=True, help_text="Format: '0000-00-00 | yyyy-mm-dd'"
    )
    phone_number = models.CharField(
        max_length=11, blank=True, null=True, help_text="Format: 09112223344"
    )

    def __str__(self):
        return f"Profile of '{self.user.username}'"
