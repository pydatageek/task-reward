from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .forms import ActionForm, ActionLevelForm
from .models import (
    Action, ActionLevel)
from .resources import ActionResource, ActionLevelResource


@admin.register(Action)
class ActionAdmin(ImportExportModelAdmin):
    """"""
    form = ActionForm
    resource_class = ActionResource

    save_on_top = True
    search_fields = ('name',)
    list_filter = ('level',)

    list_display = ('name', 'level', 'point')


@admin.register(ActionLevel)
class ActionLevelAdmin(ImportExportModelAdmin):
    """"""
    form = ActionLevelForm
    resource_class = ActionLevelResource

    save_on_top = True
    search_fields = ('name',)

    list_display = ('name', 'level_up_point', 'min_point', 'max_point')
