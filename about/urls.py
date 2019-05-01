from django.urls import path

from about import views

#creating of section "about"
app_name = 'about'
urlpatterns = [
    path('about_project', views.index, name='video'),
]
