from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок статьи')
    intro_text = models.CharField(max_length=512, verbose_name='Введение', blank=True)
    content_text = models.TextField(verbose_name='Текст статьи')
    intro_image = models.ImageField(upload_to='photos/intro/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at', ]


class ContentImage(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    content_image = models.ImageField(upload_to='photos/content/%Y/%m/%d/')

    def __str__(self):
        return self.pk

    class Meta:
        verbose_name = 'Изображение в контенте статьи'
        verbose_name_plural = 'Изображения в контенте статьи'
