from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from enrollment.models import Section

class SectionList(ListView):
    model = Section
    context_object_name = 'section'
    template_name = 'section_list.html'

class SectionCreate(CreateView):
    model = Section
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    fields = ['section_name', 'status']
    template_name = 'section_form.html'

class SectionUpdate(UpdateView):
    model = Section
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    fields = ['section_name', 'status']
    template_name = 'section_form.html'

class SectionDelete(DeleteView):
    model = Section
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    template_name = 'section_confirm_delete.html'