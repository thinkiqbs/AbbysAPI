# Generated by Django 4.0.1 on 2023-04-10 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('private_messages', '0002_rename_recipient_id_message_recipient_id_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='recipient_id_id',
            new_name='recipient',
        ),
    ]