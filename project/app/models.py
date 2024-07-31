from django.db import models


class Politices(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)  
    phone = models.CharField(max_length=15, blank=True, null=True)  
    message = models.TextField()

    def __str__(self):
        return self.name
