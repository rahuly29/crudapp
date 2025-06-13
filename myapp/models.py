from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_date = models.DateField(
        input_formats=['%d%m%Y'],
        widget=models.DateInput(format='%d%m%Y', attrs={'placeholder': 'DDMMYYYY'})
    )

    def __str__(self):
        return self.title
