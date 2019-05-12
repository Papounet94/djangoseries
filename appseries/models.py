from django.db import models


# Modèle de la série
class Serie(models.Model):

    STATUS_CHOICES = (
        ('running', 'Running'),
        ('seasonend', 'End Season'),
        ('terminated', 'End Series'),
        ('announced', 'New Season'),

    )

    title = models.CharField(max_length=25)
    airing_date = models.DateField()
    season = models.IntegerField()
    episode = models.IntegerField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)

    def __str__(self):
        s = '%02d' % self.season
        e = '%02d' % self.episode
        return '{title} - S{s}E{e} - {date} - {status}'.format(
            title=self.title,
            s=s,
            e=e,
            date=self.airing_date,
            status=self.status
        )