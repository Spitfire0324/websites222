from django.db import models

class Articles(models.Model):
    title = models.CharField('Name', max_length=50)
    announce = models.CharField('Announce', max_length=250)
    full_text = models.TextField('Document')
    date_time = models.DateTimeField('Date of publication')

    def __str__(self):
        return {self.title}

    class Meta:
        verbose_name = 'New'
        verbose_name_plural = 'News'
