from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from administrative.models import Employee

class EmployeeList(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employee_list.html'

class EmployeeCreate(CreateView):
    model = Employee
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    fields = ['first_name', 'last_name', 'type', 'status', 'username', 'password']
    template_name = 'employee_form.html'

class EmployeeUpdate(UpdateView):
    model = Employee
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    fields = ['first_name', 'last_name', 'type', 'status', 'username', 'password']
    template_name = 'employee_form.html'

class EmployeeDelete(DeleteView):
    model = Employee
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    template_name = 'employee_confirm_delete.html'

