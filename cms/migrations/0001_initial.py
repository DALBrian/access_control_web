# Generated by Django 3.2.23 on 2024-02-07 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('door_id', models.AutoField(help_text='Unique ID for this particular door', primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['door_id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(help_text='Enter the user name', max_length=50)),
                ('user_image', models.ImageField(upload_to='images/user')),
                ('introduce', models.FileField(help_text='Upload the introduce file', upload_to='introduce')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('incident_id', models.AutoField(help_text='Unique ID for this particular incident', primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/history')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('door_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.door')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.user')),
            ],
            options={
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='Face',
            fields=[
                ('face_id', models.AutoField(help_text='Unique ID for this particular face', primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images/face')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.user')),
            ],
            options={
                'ordering': ['face_id'],
            },
        ),
    ]
