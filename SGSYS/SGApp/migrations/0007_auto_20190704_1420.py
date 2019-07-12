# Generated by Django 2.1 on 2019-07-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGApp', '0006_buy_quotation'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='Brand',
            field=models.CharField(choices=[(11, 'Samsung'), (12, 'LG'), (13, 'Lloyd'), (14, 'Hitachi'), (15, 'Voltas'), (16, 'BlueStar'), (17, 'Haier'), (18, 'Daikin'), (19, 'Carrier'), (20, 'Mitsubishi')], default='Samsung', max_length=15),
        ),
        migrations.AddField(
            model_name='quotation',
            name='Query',
            field=models.TextField(blank=True, max_length=199, null=True),
        ),
        migrations.AddField(
            model_name='quotation',
            name='Tons',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
