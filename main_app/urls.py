from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('incheck/', views.incheck_index, name='incheck_index'),
    path('incheck/<int:todo_id>', views.view_todo, name='view_todo'),
    path('incheck/create/', views.create_todo, name='create_todo'),
    path('incheck/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path('incheck/<int:todo_id>/edit', views.edit_todo, name='edit_todo'),
    # Auth
    path('accounts/', views.signup, name='signup')
]