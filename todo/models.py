from django.db import models

class Todo_List(models.Model):
    id = models.IntegerField(primary_key=True)
    list = models.CharField(max_length=336)

