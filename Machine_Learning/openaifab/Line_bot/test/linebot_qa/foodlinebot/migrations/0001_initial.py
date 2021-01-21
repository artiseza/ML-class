# Generated by Django 3.1.4 on 2020-12-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default='', max_length=50)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('pic_url', models.CharField(max_length=255)),
                ('mtext', models.CharField(blank=True, max_length=255)),
                ('mdt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
