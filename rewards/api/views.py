from datetime import timedelta

from django.db.models import Q, Sum
from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from rewards.models import (
    UserLevel,
    UserActions, UserStatus)
from .serializers import (
    UserLevelSerializer,
    UserActionsSerializer, UserStatusSerializer)


# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS


class UserLevelViewset(viewsets.ModelViewSet):
    """"""
    queryset = UserLevel.objects.all()
    serializer_class = UserLevelSerializer


class UserActionsViewset(viewsets.ModelViewSet):
    """"""
    queryset = UserActions.objects.select_related('user', 'action')
    serializer_class = UserActionsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['user']


class UserStatusViewset(viewsets.ModelViewSet):
    """"""
    queryset = UserStatus.objects.select_related(
        'user', 'level').order_by('-total_points')
    serializer_class = UserStatusSerializer
    filterset_fields = ['user']
