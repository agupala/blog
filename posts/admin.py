from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    ordering = ('author', '-created')
    list_display = ('id','title', 'author', 'created', 'is_published', 'post_categories')
    list_display_links = ('id', 'title')
    search_fields = ('author', 'title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'created'
    list_filter = ('author__username', 'categories__name')
    list_editable = ('is_published',)

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])

    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)