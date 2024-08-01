from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    units = models.ManyToManyField('Units', related_name='units_set', related_query_name='unit', blank=True)

    def __str__(self):
        return self.name

class Units(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    services = models.ManyToManyField('Services', related_name='services_set', related_query_name='service', blank=True)


    def __str__(self):
        return self.name

class Politices(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

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
