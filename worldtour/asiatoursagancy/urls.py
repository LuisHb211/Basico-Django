from django.urls import path
from . import views

urlpatterns = [
  # path('', views.index, name='index'),
  path('', views.home_view, name='home'),
  path('home/', views.home_forms_view, name='home-forms'),
  path('contact/', views.contact_view, name='contact'),
  path('contact/success', views.contact_success_view, name='contact-success'),
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logouts'),
  path('register/', views.register_view, name='register'),
  path('protected/', views.ProtectedView.as_view(), name='protected'),
  
]
