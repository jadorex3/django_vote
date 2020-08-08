from django.db import models
from django.utils import timezone


class Poll(models.Model):
    """Голосование"""
    name = models.CharField(max_length=200, name='Название')
    data_start = models.DateField(name='Дата начала', default=timezone.now())
    data_end = models.DateField(name='Дата окончания')
    max_polls_to_finished = models.PositiveIntegerField(
        blank=True, null=True, name='Количество голосов до завершения')
    persons = models.ManyToManyField(
        'Person', through='Vote', through_fields=('poll', 'person'), verbose_name='Персонажи')
    is_active = models.BooleanField(default=False, name='Активно')

    def poll_is_active(self):
        if self.data_start < timezone.now() < self.data_end:
            self.is_active = True
        return self.is_active

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'


class Person(models.Model):
    """Персонаж"""
    first_name = models.CharField(max_length=100, name='Фамилия')
    last_name = models.CharField(max_length=100, name='Имя')
    patronymic = models.CharField(max_length=100, name='Отчество')
    photo = models.ImageField(name='Фото')
    age = models.PositiveSmallIntegerField(name='Возраст')
    biography = models.TextField(max_length=2000, name='Краткая биография')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class Vote(models.Model):
    """Связь между персонажами и голосованием для хранения голосов"""
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, verbose_name='Голосование')
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, verbose_name='Персонаж')
    vote = models.PositiveIntegerField(name='Количество голосов', default=0)
