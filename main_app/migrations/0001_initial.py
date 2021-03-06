# Generated by Django 3.1.6 on 2021-02-13 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('P', 'Projects'), ('H', 'Household'), ('S', 'Shopping'), ('F', 'Finances'), ('W', 'Work'), ('T', 'Trips'), ('M', 'Misc')], default='P', max_length=1)),
                ('date_created', models.DateField()),
                ('due_date', models.DateField()),
                ('body', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
