from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('members/', views.members, name='members'),
    path('members/create', views.member_create, name='members.add'),
    path('members/edit/<int:id>', views.member_edit, name='members.edit'),
    path('members/delete/<int:id>', views.member_delete, name='members.remove'),
    path('companies/', views.companies, name='companies'),
    path('companies/create', views.company_create, name='companies.add'),
    path('companies/edit/<int:id>', views.company_edit, name='companies.edit'),
    path('companies/delete/<int:id>', views.company_delete, name='companies.remove'),
]