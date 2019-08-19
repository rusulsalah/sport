from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('football/',views.football,name='football'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)