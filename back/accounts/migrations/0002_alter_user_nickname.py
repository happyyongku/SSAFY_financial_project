# Generated by Django 4.2.6 on 2024-05-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, default='anonymous', max_length=30, null=True),
        ),
    ]
