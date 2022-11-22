from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    class Genre(models.TextChoices):
        Fantasy = 'F', _('Fantasy')
        Literary = 'L', _('Literary')
        Mystery = 'M', _('Mystery')
        Non_Fiction = 'NF', _('Non_Fiction')
        Science_Fiction = 'SF', _('Science_Fiction')
        Thriller = 'T', _('Thriller')
    genre=models.CharField(max_length=2,
                            choices=Genre.choices,
                            default=Genre.choices)
    review = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
          
        ]
     )
    favorite = models.BooleanField(default=False)