# Generated by Django 3.1.4 on 2021-01-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodlinebot', '0008_auto_20201231_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_info',
            name='qtag_deep',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
    ]
