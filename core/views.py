"""Core views such as home, contact, about"""
import requests

from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView

from rest_framework.reverse import reverse_lazy as rest_reverse_lazy


class HomeView(TemplateView):
    """"""

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
