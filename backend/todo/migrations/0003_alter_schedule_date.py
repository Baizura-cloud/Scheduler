# Generated by Django 5.1 on 2024-08-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
