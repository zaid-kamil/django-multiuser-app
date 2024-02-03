from django.urls import path, re_path
from .views import *


urlpatterns = [
    # choice
    path('login/options/', login_options_view, name='login_options'),
    path('register/options/', register_options_view, name='register_options'),
    # manager
    path('manager/login/', manager_login_view, name='manager_login'),
    path('manager/register/', manager_register_view, name='manager_register'),
    path('manager/profile/', manager_profile_view, name='manager_profile'),
    path('manager/profile/update/', manager_profile_update_view, name='manager_profile_update'),
    # employee
    path('employee/login/', employee_login_view, name='employee_login'),
    path('employee/register/', employee_register_view, name='employee_register'),
    path('employee/profile/', employee_profile_view, name='employee_profile'),
    path('employee/profile/update/', employee_profile_update_view, name='employee_profile_update'),
    # customer
    path('customer/login/', customer_login_view, name='customer_login'),
    path('customer/register/', customer_register_view, name='customer_register'),
    path('customer/profile/', customer_profile_view, name='customer_profile'),
    path('customer/profile/update/', customer_profile_update_view, name='customer_profile_update'),
    # common
    path('logout/', logout_view, name='logout')
]