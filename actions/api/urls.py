from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import (
    ActionViewset, ActionLevelViewset)

router = DefaultRouter()
router.register('action', ActionViewset, basename='action')
router.register('action-level', ActionLevelViewset)

urlpatterns = [
    path('', include(router.urls)),
]
