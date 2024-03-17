from auth_system import views
from django.urls import path


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path("account", views.get_account, name="account"),
    path('account/change', views.change_info, name='change_account_info'),
    path('account/change/email', views.change_email, name="change_email"),
    path('account/change/phone', views.change_phone_number, name="change_phone_number"),
    path('account/change/password', views.change_password, name="change_password"),
]