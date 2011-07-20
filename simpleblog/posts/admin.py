from django.contrib import admin
from models import Post

def make_published(modeladmin, request, queryset):
    queryset.update(published=True)
make_published.short_description = "Publicar los siguientes posts"

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_display = ('title', 'author', 'published_date', 'publicado_hoy', 'published')
    list_filter = ('author', 'published')
    search_fields = ['title', 'text']
    actions = [make_published,]


admin.site.register(Post, PostAdmin)
