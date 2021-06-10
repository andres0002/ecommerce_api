# Generated by Django 3.1 on 2021-05-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='image',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Product Image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Product Image'),
        ),
    ]