# Generated by Django 4.0.2 on 2022-02-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='dni',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]