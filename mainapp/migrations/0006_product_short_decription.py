# Generated by Django 2.1.3 on 2018-12-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20181220_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_decription',
            field=models.CharField(max_length=30, null=True, verbose_name='Краткое описание товара'),
        ),
    ]
