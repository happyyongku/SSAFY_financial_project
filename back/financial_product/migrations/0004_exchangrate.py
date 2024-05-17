# Generated by Django 4.2.6 on 2024-05-17 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_product', '0003_alter_pensionproduct_join_way'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('cur_unit', models.CharField(max_length=10)),
                ('cur_nm', models.CharField(max_length=30)),
                ('ttb', models.FloatField()),
                ('tts', models.FloatField()),
                ('deal_base_r', models.FloatField()),
            ],
        ),
    ]
