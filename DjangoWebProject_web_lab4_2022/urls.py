"""
Definition of urls for DjangoWebProject_web_lab4_2022.
"""

from datetime import datetime
from xml.dom.minidom import Document
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('anketa/', views.anketa, name='anketa'),
    path('registration/', views.registration, name='registration'),
    path(r'^blog', views.blog, name='blog'),
    path(r'^(?P<parametr>\d+)/$', views.blogpost, name='blogpost'),
    path(r'^newpost$', views.newpost, name='newpost'),
    path(r'^videopost$', views.videopost, name='videopost'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()