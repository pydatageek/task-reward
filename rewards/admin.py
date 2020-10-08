from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from import_export.admin import ImportExportModelAdmin

from .models import (
    UserLevel,
    UserActions, UserStatus)
from .resources import UserLevelResource


@admin.register(UserLevel)
class UserLevelAdmin(ImportExportModelAdmin):
    """"""
    resource_class = UserLevelResource

    save_on_top = True
    search_fields = ('name',)

    list_display = ('name', 'level_up_point')


@admin.register(UserActions)
class UserActionAdmin(admin.ModelAdmin):
    """No add, change or delete permissions"""

    search_fields = ('user__name', 'action__name')
    list_filter = ('action__level',)
    date_hierarchy = 'timestamp'

    list_display = ('user', 'action', 'action_level', 'action_point')

    def action_level(self, obj):
        return obj.action.level.name
    action_level.short_description = _('level')
    action_level.admin_order_field = 'action__level__name'

    def action_point(self, obj):
        return obj.action.point
    action_point.short_description = _('point')
    action_point.admin_order_field = 'action__point'

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(UserStatus)
class UserStatusAdmin(admin.ModelAdmin):
    """No add, change or delete permissions"""

    search_fields = ('user__name',)
    list_filter = ('level',)

    list_display = ('user', 'level')

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
