from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Title: {self.title}"

class Advert(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url1 = models.URLField(blank=True, null=True)
    url2 = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Advert: {self.title}"

class Compensation(models.Model):
    applicants = models.IntegerField()
    received_compensation = models.IntegerField()
    total_amount = models.FloatField()

    def __str__(self):
        return f"Applicants: {self.applicants}, Received: {self.received_compensation}"

class RecommendsModel(models.Model):
    icon = models.ImageField(upload_to='icon/')
    description = models.TextField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Recommend: {self.description[:50]}..."

class SuccessWay(models.Model):
    image = models.ImageField(upload_to='user_image/')
    full_name = models.CharField(max_length=80)
    user_description = models.TextField()
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Success: {self.full_name}"

class MinistryScholarship(models.Model):
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return f"File: {self.file.name}"

class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tashkilot nomi")

    def __str__(self):
        return self.name

class CertificateCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="Sertifikat toifasi")

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=255, verbose_name="Sertifikat nomi")
    category = models.ForeignKey(CertificateCategory, on_delete=models.CASCADE, verbose_name="Sertifikat toifasi")
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Tashkilot nomi")

    def __str__(self):
        return self.name
