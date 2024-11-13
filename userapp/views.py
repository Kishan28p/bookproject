from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from auth_app.models import LoginTable
from bookapp.models import Book
from userapp.models import Cart, CartItem


# Create your views here.
def listbook(request):
    user_name=request.session['username']
    books=Book.objects.all()

    paginator=Paginator(books,4)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'user/booklist.html',{'books':books,'page':page,"user_name":user_name})

def demo_listbook(request):
    user_name=request.session['username']
    books=Book.objects.all()

    paginator=Paginator(books,4)
    page_number=request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)

    return render(request,'user/demo_booklist.html',{'books':books,'page':page,"user_name":user_name})
def detailsView(request,book_id):
    book=Book.objects.get(id=book_id)

    return render(request,'user/detailsview.html',{'book':book})

def Search_Book(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    else:
        books=[]
    context={'books':books,'query':query}
    return render(request,'user/search.html',context)

def index(request):
    return render(request,'mainpage.html')




def add_to_cart(request, book_id):

    book = Book.objects.get(id=book_id)
    if book.quantity > 0:

        user= LoginTable.objects.get(username=request.user.username)

        cart, created = Cart.objects.get_or_create(user=user)

        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('userapp:view_cart')





def view_cart(request):
    user, created = LoginTable.objects.get_or_create(username=request.user.username)

    cart, created = Cart.objects.get_or_create(user=user)

    cart_items = cart.cartitem_set.all()
    cart_item=CartItem.objects.all()

    total_price = sum(item.book.price * item.quantity for item in cart_items)

    total_items=cart_items.count()

    context = {'cart_items': cart_items,'cart_item':cart_item, 'totalprice': total_price ,'total_items':total_items}
    return render(request, 'user/cart.html', context)

def increase_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    if cart_item.quantity < cart_item.book.quantity:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('userapp:view_cart')



def decrease_quantity(request,item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('userapp:view_cart')

def remove_from_cart(request,item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
    except cart_item.DoesNotExist:
        pass

    return redirect('userapp:view_cart')

