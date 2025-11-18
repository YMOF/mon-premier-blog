
# Create your views here.
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views


def post_list(request):
    return render(request, 'blog/post_list.html', {})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
]
