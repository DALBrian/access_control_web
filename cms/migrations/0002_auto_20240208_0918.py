# Generated by Django 3.2.23 on 2024-02-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='introduce',
        ),
        migrations.AddField(
            model_name='user',
            name='user_image2',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
