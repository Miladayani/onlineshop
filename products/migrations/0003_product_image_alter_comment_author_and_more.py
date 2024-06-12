# Generated by Django 5.0.6 on 2024-06-12 06:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_cover', verbose_name='Product Image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Comment author'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='Comment text'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.CharField(choices=[('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Normal'), ('4', 'Good'), ('5', 'Perfect')], max_length=10, verbose_name="What's your rate?"),
        ),
    ]
