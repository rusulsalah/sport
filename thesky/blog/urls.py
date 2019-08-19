from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.home,name='home'),

    path('about/',views.about,name='about'),
    path('detail/<int:post_id>/',views.post_detail,name='detail'),
    path('project_index/', views.project_index, name="project_index"),
    path('project_detail<int:project_id>/', views.project_detail, name="project_detail"),
  ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)