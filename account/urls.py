from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('recovery_pass/',views.RecoveryPass.as_view(), name='recovery_pass'),
    path('active_code/', views.ActiveCode.as_view(), name='active_code'),
    path('change_pass/',views.ChangePassView.as_view(), name='change_pass')
]