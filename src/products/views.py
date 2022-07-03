from contextvars import Context
from multiprocessing import context
from urllib import request
from django.http import Http404
from django.shortcuts import render,get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawproductForm
from django.views import generic

def product_list_view(request):
    queryset=Product.objects.all() #list of objects
    context={
        "object_list": queryset
    }   
    return render(request, "product_list.html", context)
    

def something(request):
    import pdb
    pdb.set_trace()









































def product_delete_view(request,my_id):
    obj=Product.objects.get(id=my_id)
    if request.method=="POST":
        obj.delete()
        return redirect('../../../')
    context={
        "object": obj
    }
    return render(request, "product_delete.html", context)



def dynamic_lookup_view(request, my_id):
#    obj=get_object_or_404(Product, id=my_id)
#    obj=Product.objects.get(id=my_id)
    try: 
        obj=Product.objects.get(id=my_id)
    except Product.DoesNotExist:
        raise Http404
    context={
        "object": obj
    }
    return render(request, "product_detail.html", context)




def render_initial_data(request):
    initial_data={  
        'title': "My awesome title"
     }
    
    form= ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
    
    context = {
        'form': form
    }
    return render(request, "product_create.html", context)


def product_create_view(request):
    my_form = RawproductForm()
    if request.method=="POST":
     my_form=RawproductForm(request.POST)
     if my_form.is_valid():
         print(my_form.cleaned_data)
         Product.objects.create(**my_form.cleaned_data)
     else:
         print(my_form.errors)
    context={
        'form': my_form
    }
    return render(request, "product_create.html", context)



 
def product_create_view(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context={
        'form': form
    }
    return render(request, "product_create.html", context)



def product_detail_view(request):
    obj=Product.objects.get(id=40)
  #  context={
   #     'title': obj.title,
   #     'description': obj.description,
    #}
    context={
        'object': obj
    }
    return render(request, "product_detail.html", context)

