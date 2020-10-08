from django.contrib import admin

from .models import User, Group, DjangoBaseGroup

admin.site.unregister(DjangoBaseGroup)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Django's default User Admin is overriden"""
    search_fields = ('username', 'first_name', 'last_name', 'email')

    list_display = ('username', 'email', 'first_name', 'last_name')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """"""
