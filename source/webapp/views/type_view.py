from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import TypeForm
from webapp.models import Type
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .base_views import ListView


class TypeView(ListView):
    template_name = 'type/type_view.html'
    model = Type
    context_key = 'types'




class TypeCreateView(CreateView):
    template_name = 'type/create_type.html'
    model = Type
    fields = ['name']

    def get_success_url(self):
        return reverse('type_view')

    # def get(self, request, *args, **kwargs):
    #     form = TypeForm()
    #     return render(request, 'type/create_type.html', context={'form': form, })
    #
    # def post(self, request, *args, **kwargs):
    #     form = TypeForm(data=request.POST)
    #     if form.is_valid():
    #         type = Type.objects.create(
    #             name=form.cleaned_data['name']
    #         )
    #         return redirect('type_view')
    #     else:
    #         return render(request, 'type/create_type.html', context={'form': form})
    #



class TypeUpdateView(TemplateView):
    def get(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data={'name': type.name})
        return render(request, 'type/update_type.html', context={'form': form, 'type': type})

    def post(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        form = TypeForm(data=request.POST)
        if form.is_valid():
             type.name = form.cleaned_data['name']
             type.save()
             return redirect('type_view')
        else:
             return render(request, 'type/update_type.html', context={'form': form, 'type': type})




class TypeDeleteView(TemplateView):
    def  get(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        return render(request, 'type/delete_type.html', context={'type': type})
    def post(self, request, **kwargs):
        type = get_object_or_404(Type, pk=kwargs['pk'])
        try:
          type.delete()
          return redirect('type_view')
        except Exception:
          return redirect('type_view')

