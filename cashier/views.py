"""from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import CashierForm

# Create your views here.
def FA_list(request):
    query = Fees_Accounts.objects.all()
    context = {
        "object":query
    }
    return render(request, "fa_list.html", context)

def FA_detail(request, id=None):
    instance = get_object_or_404(Fees_Accounts, id =id)
    context = {
        "ins": instance,
        "title": instance.FA_name
    }
    return render(request, "fa_detail.html", context)

def FA_create(request):
    form = CashierForm()
    context = {
        "form": form
    }
    return render(request, "fa_form.html", context)

def FA_update(request):
    return HttpResponse("<h1>Home</h1>")

def FA_delete(request):
    return HttpResponse("<h1>Home</h1>")"""

from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from cashier.models import Fees_Accounts

class FAList(ListView):
    model = Fees_Accounts
    context_object_name = 'fees_accounts'
    template_name = 'fa_list.html'

class FACreate(CreateView):
    model = Fees_Accounts
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    fields = ['FA_name', 'amount']
    template_name = 'fa_form.html'

class FAUpdate(UpdateView):
    model = Fees_Accounts
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    fields = ['FA_name', 'amount']
    template_name = 'fa_form.html'

class FADelete(DeleteView):
    model = Fees_Accounts
    pk_url_kwarg = "id"
    success_url = reverse_lazy('list')
    template_name = 'fa_confirm_delete.html'