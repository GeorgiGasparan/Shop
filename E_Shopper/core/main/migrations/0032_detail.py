# Generated by Django 5.0.2 on 2024-03-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_remove_shopproduct_img2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Detail Name')),
                ('image', models.ImageField(upload_to='media', verbose_name='Detail Photo')),
                ('price', models.IntegerField(verbose_name='Price')),
            ],
        ),
    ]
