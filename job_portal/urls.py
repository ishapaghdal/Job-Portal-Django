from django.contrib import admin
from django.urls import path, include
from portal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portal/', include('portal.urls')),
     path('accounts/login/', views.login_view, name='login'),  
    path('accounts/signup/', views.signup_view, name='signup'),  
    path('accounts/logout/', views.logout_view, name='logout'),  
]
