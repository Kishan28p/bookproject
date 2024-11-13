from lib2to3.fixes.fix_input import context
from msilib.schema import ListView

from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render,redirect


from auth_app.models import LoginTable
from .forms import BookForm,AuthorForm
from .models import Book

from django.views.generic  import CreateView
# Create your views here.


# book creation
def creatBook(request):
    books = Book.objects.all()
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bookapp:admin_booklist')
    else:
        form=BookForm()

    return render(request,'admin_temp/createbook.html',{'form':form,'books':books})

# author creation
def Create_Author(request):
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('createbook/')
    else:
        form=AuthorForm()
    return render(request,'admin_temp/author.html',{'form': form})

# update created book
def updateView(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()

            return redirect('bookapp:admin_booklist')

    else:
        form=BookForm(instance=book)

    return render(request,'admin_temp/updateview.html',{'form':form,'book':book})

# delete created book
def deleteView(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method=='POST':
        book.delete()
        return redirect('bookapp:admin_booklist')
    return render(request,'admin_temp/deleteview.html',{'book':book})



def listbook(request):
    user_name = request.session['username']
    books=Book.objects.all()

    paginator=Paginator(books,4)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)




    # return redirect('authapp:login')
    return render(request,'admin_temp/booklist.html',{'books':books,'page':page,"user_name":user_name})




def detailsView(request,book_id):
    book=Book.objects.get(id=book_id)

    return render(request,'admin_temp/detailsview.html',{'book':book})

def Search_Book(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query) | Q( author__name__icontains=query))
    else:
        books=[]
    context={'books':books,'query':query}
    return render(request,'admin_temp/search.html',context)

def index(request):
    return render(request,'admin_temp/base.html')




