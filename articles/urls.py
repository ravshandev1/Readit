from django.urls import path
from .views import *

app_name = 'articles'

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('blog-single/<int:pk>', blog_single, name='blog-single'),
]
