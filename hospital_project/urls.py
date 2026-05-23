from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from patients import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('patients/', include('patients.urls')),
    path('doctors/', include('doctors.urls')),
    path('appointments/', include('appointments.urls')),
    path('pharmacy/', include('pharmacy.urls')),
    path('billing/', include('billing.urls')),
    path('wards/', include('wards.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
