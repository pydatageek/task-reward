from django.urls import path

from .views import HomeView

base_dir = 'guruable/core/'

urlpatterns = [
    path('', HomeView.as_view(
        template_name=base_dir + 'index.html'), name='home')
]
