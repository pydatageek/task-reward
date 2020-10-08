from datetime import timedelta

from django.db.models import Q, Sum
from django.utils import timezone

from rest_framework import serializers

from rewards.models import (
    UserLevel,
    UserActions, UserStatus)


class UserLevelSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = UserLevel
        fields = ('id', 'name', 'level_up_point')


class UserActionsSerializer(serializers.ModelSerializer):
    """"""
    user_obj = serializers.SerializerMethodField()
    action_obj = serializers.SerializerMethodField()

    class Meta:
        model = UserActions
        fields = (
            'id', 'user', 'user_obj', 'action', 'action_obj',
            'point_earned', 'timestamp')

    def get_user_obj(self, obj):
        return {
            'id': obj.user.id,
            'name': obj.user.username,
        }

    def get_action_obj(self, obj):
        return {
            'id': obj.action.id,
            'name': obj.action.name,
            'level': obj.action.level.name,
            'point': obj.action.point,
        }


class UserStatusSerializer(serializers.ModelSerializer):
    """"""
    user_obj = serializers.SerializerMethodField()
    level_obj = serializers.SerializerMethodField()
    is_user_eligible_today = serializers.SerializerMethodField()

    class Meta:
        model = UserStatus
        fields = ('id', 'user', 'user_obj',
                  'level', 'level_obj', 'total_points',
                  'is_user_eligible_today')

    def get_user_obj(self, obj):
        return {
            'id': obj.user.id,
            'name': obj.user.username,
            'full_name': obj.user.first_name + ' ' + obj.user.last_name,
        }

    def get_level_obj(self, obj):
        return {
            'id': obj.level.id,
            'name': obj.level.name,
        }

    def get_is_user_eligible_today(self, obj):
        """This code is supposed to return a False boolean value
        which would disable the forms. 
        TODO: not working correctly, fix it.
        """
        yesterday = timezone.now() - timedelta(hours=24)
        recent_points = UserActions.objects.filter(
            Q(user=obj.user) & Q(timestamp__gte=yesterday)
        ).aggregate(total=Sum('action__point', flat=True))

        print(recent_points)
        if recent_points['total'] > 50:  # 50 is hardcoded here, just for trials
            return False
        return True
