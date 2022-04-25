from django.contrib import admin
from api.models import Post


class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('body',)


admin.site.register(Post, PostAdmin)
