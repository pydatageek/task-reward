"""In order to import or export dummy or real data easily"""

from import_export import resources

from .models import UserLevel


class UserLevelResource(resources.ModelResource):
    """"""
    class Meta:
        model = UserLevel
