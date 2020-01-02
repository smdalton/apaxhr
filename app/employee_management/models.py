from django.db import models

# Create your hr_models here.
from django.db import models


class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()