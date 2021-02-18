# Generated by Django 3.1.6 on 2021-02-09 04:52

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
            name='Article',
            fields=[
                ('article_number', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('maintext', models.TextField()),
                ('time', models.DateTimeField()),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_number', models.AutoField(primary_key=True, serialize=False)),
                ('commentcomment_number', models.IntegerField(blank=True, null=True)),
                ('comment', models.CharField(max_length=500)),
                ('time', models.DateTimeField()),
                ('article_number', models.ForeignKey(db_column='article_number', on_delete=django.db.models.deletion.CASCADE, to='board.article')),
                ('username', models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]