from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
TITLES = (
    ('P', 'Projects'),
    ('H', 'Household'),
    ('S', 'Shopping'),
    ('F', 'Finances'),
    ('W', 'Work'),
    ('T', 'Trips'),
    ('M', 'Misc')
)
class ToDo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(
        max_length=1,
        choices=TITLES,
        default=TITLES[0][0]
        )
    date_created = models.DateField()
    due_date = models.DateField()
    body = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date_created']

IMPORTANCE = (
    ('L', 'Low'),
    ('M', 'Moderate'),
    ('H', 'High'),
)

class Importance(models.Model):
    importance = models.CharField(
        max_length=1,
        choices=IMPORTANCE,
        default=IMPORTANCE[0][0]
    )

    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_importance_display()}'



