from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / cars_photos/<filename>
    return '{0}/{1}'.format("image",filename)

class recipes(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=4000)
    ingredients = models.TextField(max_length = 10000)
    image = models.FileField(upload_to=user_directory_path, null=True, verbose_name="")

class Meta:
    db_table = 'recipes'


