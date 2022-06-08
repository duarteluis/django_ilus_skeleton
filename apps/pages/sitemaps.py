from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class PagesSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['home', 'about']

    def location(self, item):
        return reverse(item)
