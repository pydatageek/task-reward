from django.views.generic import DetailView, ListView

from .models import Action


class ActionDetailView(DetailView):
    """"""
    model = Action
