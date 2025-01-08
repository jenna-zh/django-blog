from django.contrib import admin
from blogging.models import Post, Category, PostAdmin, CategoryAdmin
from polling.models import Poll


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Poll)
