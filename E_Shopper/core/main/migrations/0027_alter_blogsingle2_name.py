# Generated by Django 4.0.5 on 2022-06-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_blogsingle2_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsingle2',
            name='name',
            field=models.CharField(max_length=50, null=float("nan"), verbose_name='BlogSingle2 name'),
        ),
    ]
