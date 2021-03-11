from django.urls import path, include
from . import views

'''
 When referring some url from here in a html page,
 we have to specify the app_name in front of the url id,
 for example <a href="{% url 'blog:detail' blog.id %}"> 
'''
app_name ='blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail')    
]