from django.shortcuts import render
from django.views.generic import ListView 
from Product.models import Product

# Create your views here.
class SearchListView(ListView):
    model = Product
    def get_queryset(self,*args,**kwargs):
        query=self.request.GET.get('q',None)
        qs=Product.objects.none()
        if query is not None:
            qs=Product.objects.filter(title__icontains=query)
        return qs
    template_name = "search/search_view.html"