from os import name

from django.contrib.auth.views import LoginView
from django.urls import path

from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('password',views.change_password,name='password'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('register',views.register,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
path('dashboard1',views.dashboard1,name='dashboard1'),
    path('fileupload',views.fileupload,name='fileupload'),
    path('myfiles',views.myfiles,name='myfiles'),
    path('apply',views.InsuranceApply,name='apply'),
    path('createpost',views.createpost,name='createpost'),
    path('results',views.results,name='results'),
path('wokersignup', views.registerUserpage, name='workersignup'),
path('doctorlogin', LoginView.as_view(template_name='doctorlogin.html'),name="doctorlogin"),
path('accounts/profile/',views.afterlogin_view,name='accounts/profile'),
path('add_scheme',views.add_scheme,name="add_scheme"),
path('view_scheme',views.view_scheme,name="view_scheme"),
path('apply1',views.apply,name="apply1"),

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)