from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')

    # class Meta:
    #     verbose_name = _("Product")
    #     verbose_name_plural = _("Products")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Product_detail", kwargs={"pk": self.pk})
