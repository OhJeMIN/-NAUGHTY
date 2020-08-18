from django.contrib import admin
from .models import UserInfo, Review, Comment, Item
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Item)