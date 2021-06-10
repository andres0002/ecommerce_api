from django.db import models

# Create your models here.

class BaseModel(models.Model):
    status = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    delete_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = 'Model Base'
        verbose_name_plural = 'Models Base'
