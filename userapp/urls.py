from django.urls import path
from . import views
app_name='userapp'
urlpatterns = [

    #product urls

    path('ubooklist',views.listbook,name='user_booklist'),
    path('demobooklist',views.demo_listbook,name='demobooklist'),
    path('detailsview/<int:book_id>/',views.detailsView,name='user_bookdetails'),
    path('search/',views.Search_Book,name='usersearch'),

    #cart urls

    path('addtocart/<int:book_id>',views.add_to_cart,name='addtocart'),
    path('viewcart',views.view_cart,name='view_cart'),
    path('increase_quantity/<int:item_id>',views.increase_quantity,name='increase_quantity'),
    path('decrease_quantity/<int:item_id>',views.decrease_quantity,name='decrease_quantity'),
    path('remove_from_cart/<int:item_id>',views.remove_from_cart,name='remove_from_cart'),

    path('',views.index,name='mainpage'),


]