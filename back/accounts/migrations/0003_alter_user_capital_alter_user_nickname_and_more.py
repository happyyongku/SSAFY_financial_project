# Generated by Django 4.2.6 on 2024-05-16 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='capital',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='special_condition',
            field=models.TextField(blank=True, null=True),
        ),
    ]