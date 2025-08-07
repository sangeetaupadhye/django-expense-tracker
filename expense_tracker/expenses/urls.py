from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_expense, name='add_expense'),
    path('all/', views.all_expenses, name='all_expenses'),
    path('edit/<int:expense_id>/', views.edit_expense, name='edit_expense'), 
    path('delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]
