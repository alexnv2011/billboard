# Generated by Django 4.1.3 on 2022-12-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='accepted',
            field=models.IntegerField(default=0),
        ),
    ]