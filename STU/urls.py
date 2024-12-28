
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, Staff_Views,Student_Views,HOD_Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.Base,name='base'),

    # Login Path
    path('',views.Login,name='login'),
    path('doLogin/',views.doLogin,name='doLogin'),

    # Logout path
    path('doLogout/',views.doLogout,name='doLogout'),

    # profile Path
    path('profile/', views.Profile, name='profile'),
    path('profile/update/',views.Profile_Update,name='profile_update'),


    # This is HOD panel URL
    path('hod/home/',HOD_Views.Home,name='hod_home'),
    path('hod/add-student/',HOD_Views.Add_Student,name='add_student'),





]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
