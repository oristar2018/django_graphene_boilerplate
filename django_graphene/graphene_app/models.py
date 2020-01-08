from django.db import models

# Create your models here.


class BaseFields(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExampleResource(BaseFields):
    example_field = models.TextField()

    def __str__(self):
        return self.example_field
