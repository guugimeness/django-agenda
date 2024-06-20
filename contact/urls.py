from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    
    # contact (CRUD)
    path('contact/<int:id>/update/', views.update, name='update'),
    path('contact/<int:id>/delete/', views.delete, name='delete'),
    path('contact/<int:id>/', views.contact, name='detail'),
    path('contact/create/', views.create, name='create'),
    
    # user
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login_view, name='login'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/update/', views.user_update, name='user-update'),
]