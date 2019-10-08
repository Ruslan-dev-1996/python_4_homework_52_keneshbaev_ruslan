from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import StatusForm
from webapp.models import Status
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .base_views import ListView


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

    # def get(self, request, *args, **kwargs):
    #     form = StatusForm()
    #     return render(request, 'status/create_status.html', context={'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = StatusForm(data=request.POST)
    #     print(form.is_valid())
    #     if form.is_valid():
    #         Status.objects.create(
    #         name=form.cleaned_data['name']
    #         )
    #         return redirect('status_view')
    #     else:
    #         return render(request, 'status/create_status.html', context={'form': form})
    #

class StatusUpdateView(TemplateView):
    def get(slef, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data={ 'name': status.name})
        return render(request, 'status/update_status.html', context={'form': form, 'status': status})

    def post(self, request, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        form = StatusForm(data=request.POST)
        if form.is_valid():
            status.name = form.cleaned_data['name']
            status.save()
            return redirect('status_view')
        else:
            return render(request, 'status/update_status.html', context={'form': form, 'status': status})


class StatusDeleteView(View):
    def get(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        return render(request, 'status/delete_status.html', context={'status': status})

    def post(self, request, *args, **kwargs):
        status = get_object_or_404(Status, pk=kwargs['pk'])
        try:
          status.delete()
          return redirect('status_view')
        except Exception:
          return redirect('status_view')