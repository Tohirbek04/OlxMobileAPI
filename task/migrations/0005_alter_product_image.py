# Generated by Django 5.0.4 on 2024-05-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_product_valyuta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='mobile'),
        ),
    ]
