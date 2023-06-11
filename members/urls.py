from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('members/create', views.member_create, name='members.add'),
    path('members/edit/<int:id>', views.member_edit, name='members.edit'),
    path('members/delete/<int:id>', views.member_delete, name='members.remove'),
]