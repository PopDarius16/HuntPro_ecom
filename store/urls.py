from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='register'),
    # path('register', views.register, name='register'),
    # path('product/<int:pk>', views.product, name='product')
]