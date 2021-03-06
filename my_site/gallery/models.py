from django.db import models


class Album(models.Model):
    title = models.CharField(max_length = 50)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.title

class Img(models.Model):
    alb = models.ForeignKey(Album,
                            default=None,
                            on_delete=models.CASCADE,
                           )
    # Параметр upload_to: файлы будут автоматически загружены в MEDIA_ROOT/images/
    image = models.ImageField(upload_to ='images/')

    def __str__(self):
        return self.alb.title

