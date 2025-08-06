from django.db import models

class MajorCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ListDocument(models.Model):
    file = models.FileField(upload_to='list-document/')

class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Table(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    major = models.ForeignKey(MajorCategory, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()

    def __str__(self):
        return self.name
