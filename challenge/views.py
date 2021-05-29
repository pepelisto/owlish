from django.shortcuts import render
from django.views.generic import ListView
from .models import Customer


class CustomersList(ListView):

    model = Customer
    template_name = 'list.html'
    context_object_name = 'customers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def customer_detail(request, pk):
    customer = Customer.objects.get(pk=pk)
    return render(request, 'detail.html', {'customer': customer})

