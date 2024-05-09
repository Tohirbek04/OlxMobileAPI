# Generated by Django 5.0.4 on 2024-05-07 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='status', to='task.status'),
            preserve_default=False,
        ),
    ]
