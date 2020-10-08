from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    UserLevelViewset, UserActionsViewset, UserStatusViewset)

router = DefaultRouter()
router.register('user-level', UserLevelViewset, basename='user-level')
router.register(
    'user-actions', UserActionsViewset, basename='user-actions')
router.register('user-status', UserStatusViewset, basename='user-status')

urlpatterns = [
    path('', include(router.urls)),
]
