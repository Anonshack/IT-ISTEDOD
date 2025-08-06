from django.db import models

class UsefulProgram(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    url = models.URLField()

    class Meta:
        verbose_name = "Useful Program"
        verbose_name_plural = "Useful Programs"

    def __str__(self):
        return self.title


class OnlineResource(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='OnlineResource/', blank=True, null=True)
    url = models.URLField()

    class Meta:
        verbose_name = "Online Resource"
        verbose_name_plural = "Online Resources"

    def __str__(self):
        return self.title


class VideoResource(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    url = models.URLField()

    class Meta:
        verbose_name = "Video Resource"
        verbose_name_plural = "Video Resources"

    def __str__(self):
        return self.title
