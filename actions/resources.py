"""In order to import or export dummy or real data easily"""

from import_export import resources

from .models import Action, ActionLevel


class ActionResource(resources.ModelResource):
    """"""
    class Meta:
        model = Action


class ActionLevelResource(resources.ModelResource):
    """"""
    class Meta:
        model = ActionLevel
