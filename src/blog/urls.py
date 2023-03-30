from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('', views.Home, name='home'),
    path('About/', views.About, name='About'),
    path('<slug:slug>',views.single_post, name='single_post'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)