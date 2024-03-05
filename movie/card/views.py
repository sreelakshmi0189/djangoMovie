
from django.shortcuts import render

from card.models import Cards

from card.forms import Cardsform
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.


# def home(request):
#     k = Cards.objects.all()
#     return render(request,'home.html',{'b': k})

class MovieList(ListView):     #ListView displays all objects/records retrieving from a model.
    model=Cards
    template_name="home.html"
    context_object_name="b"




# def addmovie(request):
#     if(request.method=="POST"):
#         t=request.POST['t']
#         d=request.POST['d']
#         y=request.POST['y']
#         i=request.FILES['i']
#         b=Cards.objects.create(title=t,desc=d,year=y,image=i)
#         b.save()
#         return home(request)
#
#     return render(request,'addmovie.html')


class Movieadd(CreateView):   #createview displays a form adding new object and handles form submission
    model=Cards
    template_name="addmovie.html"
    fields='__all__'
    success_url=reverse_lazy("card:home")




# def viewmovies(request,p):
#         b=Cards.objects.get(id=p)
#         return render(request, 'viewmovies.html', {'b': b})

class MovieDetail(DetailView):
    model=Cards
    template_name="viewmovies.html"
    context_object_name="b"



# def moviedelete(request,p):
#     b =Cards.objects.get(id=p)
#     b.delete()
#     return home(request)

class Moviedelete(DeleteView):
    model = Cards
    template_name = "delete.html"
    success_url = reverse_lazy('card:home')



# def movieupdate(request,p):
#     b=Cards.objects.get(id=p)
#     if (request.method == "POST"):  #After submission
#         form=Cardsform(request.POST,request.FILES,instance=b)  #Creates form object initialized with values inside request.POST
#         if form.is_valid():
#             form.save()  # save the form object inside DB table
#         return home(request)
#
#     form=Cardsform(instance=b)
#     return render(request,"update.html",{"form":form})



class Movieupdate(UpdateView):
    model=Cards
    template_name ="update.html"
    fields='__all__'
    success_url=reverse_lazy('card:home')

