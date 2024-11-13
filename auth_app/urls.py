from django.urls import path

from . import views
app_name='authapp'
urlpatterns = [
    path('',views.Register,name='register'),
    path('login/',views.login,name='login'),
    path('logout',views.logOut,name='logout')

]