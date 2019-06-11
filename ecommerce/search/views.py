from django.shortcuts import render
from django.views.generic import ListView 
from Product.models import Product
from django.db.models import Q

# Create your views here.
class SearchListView(ListView):
    model = Product
    template_name = "search/search_view.html"
    def get_queryset(self,*args,**kwargs):
        query=self.request.GET.get('q',None)
        qs=Product.objects.none()
        if query is not None:
            lookup=Q(title__icontains=query) | Q(description__icontains=query)
            qs=Product.objects.filter(lookup).distinct()
        return qs