# Generated by Django 3.1.6 on 2021-02-06 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fullname',
            field=models.CharField(default='null', max_length=20, verbose_name='fullname'),
            preserve_default=False,
        ),
    ]