from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    short_description = models.TextField(blank=True, verbose_name=_('Short Description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('Price'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    image = models.ImageField(verbose_name=_('Product Image'), upload_to="product/product_cover", blank=True)

    date_created = models.DateField(default=timezone.now, verbose_name=_('Date Created'))
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args={self.pk})


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Product') )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Comment author')
    )
    body = models.TextField(verbose_name=_('Comment text'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_("What's your rate?"))

    date_created = models.DateField(auto_now_add=True, verbose_name=_('Date Created'))
    date_modified = models.DateField(auto_now=True)
    active = models.BooleanField(default=True, verbose_name=_('Active'))

    objects = models.Manager()
    active_comments_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])