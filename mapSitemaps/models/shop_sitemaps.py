from django.db import models

class ShopSitemap(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    shop_id = models.IntegerField(null=True, blank=True)
    checked = models.BooleanField(default=False)

    class Meta:
        db_table = 'shop_sitemaps'
