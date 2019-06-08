from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView ,DetailView,DeleteView ,CreateView ,UpdateView
from .models import Product,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CommentForm
from django.contrib.auth import get_user

# Create your views here.


class ProductListView(ListView):
    model = Product
    qs=Product.objects.all()
    template_name = "Product/Product_list.html"

class ProductDetailView(DetailView):
    model=Product
    context_object_name='product'
    template_name = "Product/product_detail.html"
    def get_object(self):
        return get_object_or_404(Product,pk=self.kwargs.get('pk'))

class DeleteProductView(DeleteView,LoginRequiredMixin):
    model = Product
    success_url=reverse_lazy('home')

class CreateProductView(LoginRequiredMixin,CreateView):
    model=Product
    fields=('title','description','price','image')
    redirect_field_name ='Product/Product_list.html'

class UpdateProductView(LoginRequiredMixin,UpdateView):
    model = Product
    fields=['title','description','image','price']
    template_name='Product/product_update.html'
    redirect_field_name='Product/product_detail.html'

# comment section
@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    Product_pk=comment.product.pk
    comment.delete()
    return redirect('product_detail',pk=Product_pk)

@login_required
def add_comment(request,pk):
    product=get_object_or_404(Product,pk=pk)
    form=CommentForm()
    if request.method == 'POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=get_user(request)
            comment.product=product
            comment=form.save()
            return redirect('product_detail',pk=product.pk)
        else:
            form=CommentForm()
    return render(request,'Product/comment_form.html',{'form':form,'product':product})

class comment_detail(DetailView,LoginRequiredMixin):
    model=Comment
    context_object_name='comment'
    template_name = "Product/comment_detail.html"
    def get_object(self):
        return get_object_or_404(Comment,pk=self.kwargs.get('pk'))
