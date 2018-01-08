from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from registrar.models import SHS_Subjects

class SHS_SubjList(ListView):
    model = SHS_Subjects
    context_object_name = 'shs_subs'
    template_name = 'shsSubj_list.html'

class SHS_SubjCreate(CreateView):
    model = SHS_Subjects
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    fields = ['SHS_subjectName', 'SHS_desc', 'SHS_trackStatus']
    template_name = 'shsSubj_form.html'

class SHS_SubjUpdate(UpdateView):
    model = SHS_Subjects
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    fields = ['SHS_subjectName', 'SHS_desc', 'SHS_trackStatus']
    template_name = 'shsSubj_form.html'

class SHS_SubjDelete(DeleteView):
    model = SHS_Subjects
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    template_name = 'shsSubj_confirm_delete.html'