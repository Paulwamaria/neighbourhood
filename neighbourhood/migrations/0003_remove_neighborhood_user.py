# Generated by Django 2.2.6 on 2019-10-26 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0002_auto_20191026_0839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='user',
        ),
    ]
