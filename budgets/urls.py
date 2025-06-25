from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_budgets, name='my_budgets'),
    path('budgets/add/', views.add_budget, name='add_budget'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/add/', views.add_transaction, name='add_transaction'),
    path('transactions/delete/<int:pk>/', views.delete_transaction, name='delete_transaction'),
    path('edit/<int:pk>/', views.edit_budget, name='edit_budget'),
    path('transactions/edit/<int:pk>/', views.edit_transaction, name='edit_transaction'),
    path('all_budgets/', views.all_budgets, name='all_budgets'),
    path('admin-page/', views.admin_only_page, name='admin_only_page'),
    path('delete/<int:pk>/', views.delete_budget, name='delete_budget'),
]
