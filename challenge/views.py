from django.shortcuts import render
from django.views.generic import ListView
from .models import Customer


class CustomersList(ListView):
    """
    Returns the list of all the customers and their related information
    stored in the database
    """
    model = Customer
    template_name = 'list.html'
    context_object_name = 'customers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def customer_detail(request, pk):
    """
    Returns the details of a single customer by its id
    """
    customer = Customer.objects.get(pk=pk)
    return render(request, 'detail.html', {'customer': customer})

