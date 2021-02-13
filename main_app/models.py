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
    completed = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date_created']



