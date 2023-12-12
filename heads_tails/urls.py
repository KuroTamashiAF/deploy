from django.urls import path
from . import views

urlpatterns = [
    path('', views.heads_tails, name="heads_tails"),
    path('print_all_value/<int:n>', views.print_all_value, name="print_all_value"),
]
