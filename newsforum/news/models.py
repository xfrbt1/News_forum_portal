from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=2500)
    time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'NEWS'
        verbose_name_plural = "NEWS"
        ordering = ["-time"]