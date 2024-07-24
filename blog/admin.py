from django.contrib import admin
from blog.models import Tag, Post

# Register your models here.
# Still need to fix a bug here
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')

admin.site.register(Tag)
admin.site.register(PostAdmin)
