"""tamircity_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt import views as jwt_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/reservations/', include('reservations.api.urls'), name='reservations'),
    path('api/v1/comments/', include('comments.api.urls'), name='comments'),
    path('api/v1/favourites/', include('favourites.api.urls'), name='favourites'),
    path('api/v1/accounts/', include('accounts.api.urls'), name='accounts'),
    path('api/v1/device-types/', include('device_types.api.urls'), name='device_types'),
    path('api/v1/brands/', include('brands.api.urls'), name='brands'),
    path('api/v1/models/', include('models.api.urls'), name='models'),
    path('api/v1/payments/', include('payments.api.urls'), name='payments'),
    path('api/v1/newsletters/', include('newsletters.api.urls'), name='newsletters'),
    path('api/v1/service-types/', include('service_types.api.urls'), name='service_types'),
    path('api/v1/contacts/', include('contacts.api.urls'), name='contacts'),
    path('api/v1/expertise-forms/', include('expertise_forms.api.urls'), name='expertise_forms'),
    path('api/v1/technical-services/', include('technical_services.api.urls'), name='technical_services'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
#] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()