# Generated by Django 4.0.4 on 2022-05-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dname',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]