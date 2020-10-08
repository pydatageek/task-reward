from django.urls import path

from .views import ActionDetailView

base_dir = 'guruable/actions/'

urlpatterns = [
    path('actions/', ActionDetailView.as_view(
        template_name=base_dir + 'action-detail.html'),
        name='action-detail')
]
