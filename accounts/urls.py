from django.urls import path
from .views import register
from .views import login
from .views import logout
from .views import activate
from .views import dashboard
from .views import forgotpassword
from .views import resetpassword_validate
from .views import resetpassword
from .views import my_orders
from .views import edit_profile
from .views import change_password
from .views import order_detail

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', dashboard, name='dashboard'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('resetpassword_validate/<uidb64>/<token>/', resetpassword_validate, name='resetpassword_validate'),
    path('forgotpassword/', forgotpassword, name='forgotpassword'),
    path('resetpassword', resetpassword, name='resetpassword'),
    path('my_orders/', my_orders, name='my_orders'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('change_password/', change_password, name='change_password'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail')
]