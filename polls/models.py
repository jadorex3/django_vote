from django.db import models
from django.utils import timezone


class Person(models.Model):
    """Персонаж"""
    first_name = models.CharField('Фамилия', max_length=100)
    last_name = models.CharField('Имя', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    photo = models.ImageField('Фото')
    age = models.PositiveSmallIntegerField('Возраст')
    biography = models.TextField('Краткая биография', max_length=2000)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class Poll(models.Model):
    """Голосование"""
    name = models.CharField('Название', max_length=200)
    data_start = models.DateField('Дата начала', default=timezone.now())
    data_end = models.DateField('Дата окончания')
    max_polls_to_finished = models.PositiveIntegerField(
        'Количество голосов до завершения', blank=True, null=True)
    # persons = models.ManyToManyField(
    #     Person, verbose_name='Персонажи')
    persons = models.ManyToManyField(
        Person, through='Vote', through_fields=('poll', 'person'), verbose_name='Персонажи')
    is_active = models.BooleanField('Активно', default=True, )

    def poll_is_active(self):
        if self.data_start < timezone.now() < self.data_end:
            self.is_active = True
        return self.is_active

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'


class Vote(models.Model):
    """Связь между персонажами и голосованием для хранения голосов"""
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, verbose_name='Голосование')
    person = models.ForeignKey(
        Person, on_delete=models.CASCADE, verbose_name='Персонаж')
    vote = models.PositiveIntegerField('Количество голосов', default=0)
