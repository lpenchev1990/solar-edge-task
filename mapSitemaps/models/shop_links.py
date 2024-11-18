from django.db import models
from .shop_sitemaps import ShopSitemap  # Импортирай връзката, ако има такава

class ShopLink(models.Model):
    id = models.AutoField(primary_key=True)
    shop_id = models.IntegerField(null=True, blank=True)  # Връзка към ShopSitemap
    link = models.URLField()
    mapped = models.BooleanField(default=False)

    class Meta:
        db_table = 'shop_links'
