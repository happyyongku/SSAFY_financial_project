# Generated by Django 4.2.6 on 2024-05-17 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pensionproduct',
            name='btrm_prft_rate_1',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pensionproduct',
            name='btrm_prft_rate_2',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pensionproduct',
            name='btrm_prft_rate_3',
            field=models.FloatField(null=True),
        ),
    ]
