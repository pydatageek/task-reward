from rest_framework import renderers, viewsets

from rewards.models import UserStatus
from actions.models import Action, ActionLevel
from .serializers import ActionSerializer, ActionLevelSerializer

base_dir = 'guruable/actions/'


def get_current_user(request):
    return request.user


class ActionViewset(viewsets.ModelViewSet):
    """"""
    serializer_class = ActionSerializer

    def get_queryset(self):
        """Actions are listed depending on the reputation 
        (total_points earned) by the user.
        """
        qs = Action.objects.select_related('level')

        level_up_point = ActionLevel.objects.order_by(
            'level_up_point').values_list('level_up_point', flat=True).first()

        user = self.request.user

        if user.is_anonymous:
            return qs.filter(level__level_up_point__lte=level_up_point)

        totalpoints = 0
        if UserStatus.objects.filter(user=user).exists():
            print('userstatus: {user.userstatus}')
            totalpoints = user.userstatus.total_points
        if totalpoints < level_up_point:
            totalpoints = level_up_point
        return qs.filter(level__level_up_point__lte=totalpoints)


class ActionLevelViewset(viewsets.ModelViewSet):
    """"""
    queryset = ActionLevel.objects.all()
    serializer_class = ActionLevelSerializer
