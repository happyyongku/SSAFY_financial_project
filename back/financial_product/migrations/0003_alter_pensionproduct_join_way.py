# Generated by Django 4.2.6 on 2024-05-17 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_product', '0002_alter_pensionproduct_btrm_prft_rate_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pensionproduct',
            name='join_way',
            field=models.TextField(null=True),
        ),
    ]