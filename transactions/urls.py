from django.urls import path
from . import views
app_name = 'transactions'

urlpatterns = [
    path('store/' , views.BookStore , name='bookstore'),
    path('show/<int:id>/' , views.BookShow , name='bookshow'),
    path('link/' , views.ShowLink , name='link'),
    path('edit/<int:id>/' , views.editbook , name='editbook'),
    # path('delete/<int:id>/' , views.delelebook , name='delete'),
]
