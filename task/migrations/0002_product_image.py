# Generated by Django 5.0.4 on 2024-05-07 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, max_length=5, upload_to='mobile'),
            preserve_default=False,
        ),
    ]
