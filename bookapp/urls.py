
from django.urls import path, include
from .import views
app_name='bookapp'
urlpatterns = [
    path("createbook/",views.creatBook,name='createbook'),
    path("booklist/",views.listbook,name='admin_booklist'),

    path('detailsview/<int:book_id>/',views.detailsView ,name='details'),
    path('updateview/<int:book_id>/',views.updateView,name='update'),
    path('deleteview/<int:book_id>',views.deleteView,name='delete'),
    path('index',views.index),
    path('author',views.Create_Author,name='author'),
    path('search/',views.Search_Book,name='search'),





]

