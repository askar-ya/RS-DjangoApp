from datetime import datetime

from django.db import models


class MainChapters(models.Model):
    """Разделы подкатегорий"""
    name = models.CharField('Название', max_length=30)
    class Meta:
        db_table = 'main_chapters'

    def __str__(self):
        return self.name


class Categories(models.Model):
    """Категории авторов рилсов"""
    main_chapter = models.ForeignKey(MainChapters, on_delete=models.CASCADE)
    #main_chapter = models.CharField('Название раздела подкатегорий', max_length=30)
    name = models.CharField('Название категории', max_length=100)
    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Authors(models.Model):
    """Авторы рилсов"""
    nick = models.CharField('Ник инстаграмм', max_length=30)

    description = models.TextField('Описание профиля', default='')
    reels_count = models.IntegerField('Кол-во рилсов', default=0)
    subscribers = models.IntegerField('Кол-во подписчиков', default=0)
    subscriptions = models.IntegerField('Кол-во подписок', default=0)


    add_stamp = models.DateTimeField('Время добавления', default=datetime.now)
    updated_stamp = models.DateTimeField('Время обновления', default=datetime.now)
    last_rell = models.IntegerField('Последний рилс', default=0)
    new = models.BooleanField("Новый", default=True)

    categories = models.ManyToManyField(Categories)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.nick


class Reels(models.Model):
    """Рилсы авторов"""
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    url = models.CharField('url на видео рилса', max_length=44)
    likes = models.IntegerField('Кол-во лайков')
    comments = models.IntegerField('Кол-во комментариев')
    views = models.IntegerField('Кол-во просмотров')
    description = models.TextField('Описание рилса')

    published_stamp = models.DateTimeField('Дата публикации', default=datetime.now)
    updated_stamp = models.DateTimeField('Время обновления', default=datetime.now)
    new = models.BooleanField("новый", default=True)

    class Meta:
        db_table = 'reels'
