from django.contrib.syndication.views import Feed
from models import Post
from django.core.urlresolvers import reverse

class LatestEntriesFeed(Feed):
    title = "Simple Blog Feed"
    link = "/feed/"
    description = "Esto es un feed ahi"

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse("post_detail", args=[item.id])
