from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import StatusForm
from webapp.models import Status
from django.views import View

from django.views.generic.edit import CreateView

from .base_views import ListView, UpdateView, DeleteView


class StatusView(ListView):
    template_name = 'status/status_view.html'
    model = Status
    context_key = 'statuses'



class StatusCreateView(CreateView):
    template_name = 'status/create_status.html'
    model = Status
    fields = ['name']

    def get_success_url(self):
        return reverse('status_view')

class StatusUpdateView(UpdateView):
    model = Status
    template_name = 'status/update_status.html'
    form_class = StatusForm
    context_object_name = 'status'

    def get_redirect_url(self):
        return reverse('status_view')



class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'status/delete_status.html'
    context_object_name = 'status'

    def get_redirect_url(self):
        return reverse('status_view')

