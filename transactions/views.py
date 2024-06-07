from django.shortcuts import render , redirect
from . forms import BookForm , EditForm
from . models import BookModel , Categorymodel

def BookStore(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request , 'bookstore.html' , {'form':form})

def ShowLink(request):
    data = Categorymodel.objects.all()
    return render(request , 'showlink.html' , {'data':data})

def BookShow(request , id):
    data = BookModel.objects.get(pk=id)
    return render(request , 'bookshow.html' , {'dt':data})

def editbook(request , id):
    book = BookModel.objects.get(pk = id)
    data = EditForm(instance=book)
    if request.method == 'POST':
        data=EditForm(request.POST , instance=book)
        if data.is_valid():
            data.save()
            return redirect('bookshow')
    return render(request , 'editbook.html' , {'form':data})

def borrowbook(request , id):
    book=BookModel.objects.get(pk=id)
    
