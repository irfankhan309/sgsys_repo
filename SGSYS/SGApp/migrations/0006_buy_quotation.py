# Generated by Django 2.1 on 2019-07-01 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGApp', '0005_aclist_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=99)),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
