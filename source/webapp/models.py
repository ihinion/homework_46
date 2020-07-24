from django.db import models

STATUS_CHOICES = [('new', 'New'), ('in_progress', 'In progress'), ('done', 'Done')]


class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name='Description')
    status = models.TextField(max_length=15, verbose_name='Status', default=STATUS_CHOICES[0][0],
                              choices=STATUS_CHOICES)
    finish_date = models.DateField(max_length=10, null=True, blank=True, verbose_name='Finished')

    def __str__(self):
        return f'{self.pk}. {self.description}'
