from django.urls import path
from . import views



urlpatterns = [

    # Department URLs
    path('add-department/', views.department_create, name='department_create'),
    path('departments/', views.department_list, name='department_list'),
    

    # Employee URLs
    path('add-employee/', views.employee_create, name='employee_create'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employee/edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('employee/delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('',views.home,name='home'),
]
