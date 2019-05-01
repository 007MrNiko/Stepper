from django.urls import path

from weather import views

#creating of the weather_app
app_name = 'weather'
urlpatterns = [
    path('your_weather', views.index, name='weather'),
]
