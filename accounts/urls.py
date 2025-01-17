from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('register/', views.register , name='register'),
    path('activate/<uidb64>/<token>/',views.activate , name='activate'),
    path('login/' , views.login , name='login'),
    path('logout/' , views.logout , name='logout'),
]
