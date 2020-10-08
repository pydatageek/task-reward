from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Action, ActionLevel


class ActionForm(forms.ModelForm):
    """"""

    point = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'type': 'number', 'min': '1', 'max': '15', 'id': 'point_range'}),
        required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Action
        fields = ('name', 'level', 'point')


class ActionLevelForm(forms.ModelForm):
    """"""

    min_point = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'type': 'number', 'min': '1', 'max': '11', 'id': 'min_point_range'}),
        required=True)
    max_point = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'type': 'number', 'min': '3', 'max': '15', 'id': 'max_point_range'}),
        required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ActionLevel
        fields = ('name', 'level_up_point', 'min_point', 'max_point')
