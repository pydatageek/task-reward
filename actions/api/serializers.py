from rest_framework import serializers

from actions.models import Action, ActionLevel


class ActionSerializer(serializers.ModelSerializer):
    """"""
    level_obj = serializers.SerializerMethodField()

    class Meta:
        model = Action
        fields = ('id', 'name', 'level', 'level_obj', 'point')

    def get_level_obj(self, obj):
        return {
            'id': obj.level.id,
            'name': obj.level.name,
        }


class ActionLevelSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = ActionLevel
        fields = (
            'id', 'name', 'level_up_point', 'min_point', 'max_point')
