# Generated by Django 4.0.1 on 2023-05-08 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_answer_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='title',
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]