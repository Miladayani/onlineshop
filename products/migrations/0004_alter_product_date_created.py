# Generated by Django 5.0.6 on 2024-06-13 11:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]