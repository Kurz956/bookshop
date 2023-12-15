from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=70)     # поле типа CharField с максимальной длиной значения 70 символов
    rating = models.IntegerField()      # рейтинг книги, поле типа IntegerField

    def __str__(self):
        return f'{self.title} - {self.rating}'