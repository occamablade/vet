from django.contrib.auth import get_user_model
from django.db import models
from core.models import CreatedModel


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Pet(CreatedModel):
    name = models.TextField(
        'Имя питомца',
        help_text='Введите имя питомца'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True)
    owner = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='pets',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='pets',
        verbose_name='Группа',
        help_text='Группа, к которой будет относиться питомец'
    )
    image = models.ImageField(
        'Фото питомца',
        upload_to='pets/',
        blank=True
    )

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария',
        related_name='comments'
    )
    text = models.TextField(
        'Текст',
        help_text='Текст нового комментария'
    )
    created = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    class Meta:
        ordering = ['created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:50]
