from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books, name="all_books_url"),
  #  path('shows/<int:id>/', views.get_show_detail, name="show_url"),
]