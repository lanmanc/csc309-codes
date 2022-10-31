
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from stores.models import Store


# class StoresView(TemplateView):
#     template_name = 'stores/stores.html'
#
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs) | \
#             {'stores': Store.objects.all()}


class StoresView(ListView):
    template_name = 'stores/stores.html'
    queryset = Store.objects.all()
    context_object_name = 'stores'
