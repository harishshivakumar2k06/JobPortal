from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('jobs/', views.job_list, name='jobs'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('profile/', views.profile, name='profile'),
    path('upload-resume/', views.upload_resume, name='upload_resume'),

    path(
    'admin-dashboard/',
    views.admin_dashboard,
    name='admin_dashboard'
),
]