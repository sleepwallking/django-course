from django.db import models
from django.urls import reverse


class Cars(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Автомобили'
        verbose_name_plural = 'Автомобили'
        ordering = ['time_create', 'title']

