# Generated by Django 4.2.5 on 2024-02-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_director',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]
