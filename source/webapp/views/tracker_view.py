from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import TrackerForm
from webapp.models import Tracker
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView

from webapp.views.base_detailed import DetailView


class IndexView(ListView):
    template_name = 'tracker/index.html'
    model = Tracker
    context_object_name = 'trackers'
    ordering = ['-created_at']
    paginate_by = 2
    paginate_orphans = 1




class TrackerView(DetailView):
    template_name = 'tracker/detailed.html'
    model = Tracker
    context_key = 'tracker'




class TrackerCreateView(CreateView):
    template_name = 'tracker/create.html'
    model = Tracker
    fields = ['summary', 'description', 'status', 'type']
    def get_success_url(self):
        return reverse('tracker_view', kwargs={'pk': self.object.pk})







 class TrackerUpdateView(UpdateView):


    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Tracker, pk=kwargs.get('pk'))
        form = TrackerForm(data={
            'summary': issue.summary,
            'description': issue.description,
            'status': issue.status_id,
            'type': issue.type_id
        })
        return render(request, 'tracker/update.html', context={'form': form, 'issue': issue})

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Tracker, pk=kwargs.get('pk'))
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            issue.summary = form.cleaned_data['summary']
            issue.description = form.cleaned_data['description']
            issue.status = form.cleaned_data['status']
            issue.type = form.cleaned_data['type']
            issue.save()
            return redirect('tracker_view', pk=issue.pk)
        else:
            return render(request, 'tracker/update.html', context={'form': form, 'issue': issue})



class TrackerDeleteView(View):
    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Tracker, pk=kwargs['pk'])
        return render(request, 'tracker/delete.html', context={'issue': issue})

    def post(self, request, *args, **kwargs):
         issue = get_object_or_404(Tracker, pk=kwargs['pk'])
         issue.delete()
         return redirect('index')

