# Generated by Django 4.2.6 on 2024-05-19 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangrate',
            name='date',
            field=models.DateField(),
        ),
    ]