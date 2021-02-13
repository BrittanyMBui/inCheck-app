from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('incheck/', views.incheck_index, name='incheck_index'),
    path('accounts/', views.signup, name='signup')
]