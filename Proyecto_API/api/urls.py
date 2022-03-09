from django.urls import path
from .views import CompanyView, EmployeeView

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='companies_list'),
    path('companies/<int:id>', CompanyView.as_view(), name='companies_process'),

    path('employees/', EmployeeView.as_view(), name='employees_list')
]