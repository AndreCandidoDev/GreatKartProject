from django.urls import path
from .views import register
from .views import login
from .views import logout
from .views import activate
from .views import dashboard
from .views import forgotpassword
from .views import resetpassword_validate
from .views import resetpassword

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
]