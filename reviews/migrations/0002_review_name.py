# Generated by Django 3.2.13 on 2022-09-30 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='name',
            field=models.CharField(default='', max_length=10, null=True),
        ),
    ]
