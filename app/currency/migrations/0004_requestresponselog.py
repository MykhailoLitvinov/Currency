# Generated by Django 3.2.7 on 2021-11-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_auto_20211109_0913'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('request_method', models.CharField(max_length=255)),
                ('time', models.DecimalField(decimal_places=4, max_digits=6)),
            ],
        ),
    ]
