from django.db import models


class Department(models.Model):
    title = models.CharField('Department Title', max_length=128, unique=True)
    opening_date = models.DateField('Opening Date')

    def __str__(self):
        return self.title


class Designation(models.Model):
    title = models.CharField('Designation Title', max_length=128, unique=True)
    department = models.ForeignKey(Department, models.SET_NULL, null=True)

    def __str__(self):
        return self.title
