from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.base import View


class ListView(TemplateView):
    context_key = 'objects'
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[self.context_key] = self.get_objects()
        return context

    def get_objects(self):
        return self.model.objects.all()

class UpdateView(View):
    form_class = None
    template_name = None
    redirect_url = ''
    model = None
    pk_kwargs_url = 'pk'
    context_object_name = None
    object = None

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        form = self.form_class(instance=obj)
        return render(request, self.template_name, context={'form': form, self.context_object_name: obj})

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        form = self.form_class(instance=obj, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_redirect_url(self):
        return self.redirect_url

    def form_valid(self, form):
        self.object = self.get_object()
        form.save()
        return redirect(self.get_redirect_url())

    def form_invalid(self, form):
        return render(self.request, self.template_name, context={'form': form})

    def get_object(self):
        pk = self.kwargs.get(self.pk_kwargs_url)
        obj = get_object_or_404(self.model, pk=pk)
        return obj

class DeleteView(View):
    template_name = None
    redirect_url = ''
    model = None
    pk_kwargs_url = 'pk'
    context_object_name = None
    object = None
    error_page = None

    def get(self, request, *args, **kwargs):
        object = self.get_object()
        return render(request, self.template_name, context={self.context_object_name: object})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            return redirect(self.get_redirect_url())
        except:
            return render(request, self.error_page)

    def get_object(self):
        pk = self.kwargs.get(self.pk_kwargs_url)
        obj = get_object_or_404(self.model, pk=pk)
        return obj

    def get_redirect_url(self):
        return self.redirect_url