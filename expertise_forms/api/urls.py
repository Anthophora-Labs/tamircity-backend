from django.urls import path
from expertise_forms.api.views import (
                            ExpertiseTVCreateAPIView,
                            ExpertiseWatchCreateAPIView,
                            ExpertiseConsoleCreateAPIView,
                             ExpertisePhoneCreateAPIView,
                             ExpertisePcCreateAPIView,
                             ExpertiseConsoleListAPIView,
                             ExpertisePhoneListAPIView,
                             ExpertisePcListAPIView,
                            ExpertiseWatchDetailAPIView,
                            ExpertiseTVDetailAPIView,
                            ExpertiseConsoleDetailAPIView,
                            ExpertisePcDetailAPIView,
                            ExpertisePhoneDetailAPIView,
)

app_name = 'expertise_forms'


urlpatterns = [
    path('expertise-tv', ExpertiseTVCreateAPIView.as_view(), name='create_expertise_tv'),
    path('expertise-watch', ExpertiseWatchCreateAPIView.as_view(), name='create_expertise_watch'),
    path('create-console', ExpertiseConsoleListAPIView.as_view(), name='create_expertise_console'),
     path('list-console', ExpertiseConsoleCreateAPIView.as_view(), name='list_expertise_console'),
     path('create-phone', ExpertisePhoneCreateAPIView.as_view(), name='create_expertise_phone'),
     path('list-phone', ExpertisePhoneListAPIView.as_view(), name='list_expertise_phone'),
     path('create-pc', ExpertisePcCreateAPIView.as_view(), name='create_expertise_pc'),
     path('list-pc', ExpertisePcListAPIView.as_view(), name='create_expertise_pc'),
     path('detail-phone/<pk>', ExpertisePhoneDetailAPIView.as_view(), name='detail_phone'),
    path('detail-tv/<pk>', ExpertiseTVDetailAPIView.as_view(), name='detail_tv'),
    path('detail-console/<pk>', ExpertiseConsoleDetailAPIView.as_view(), name='detail_console'),
    path('detail-watch/<pk>', ExpertiseWatchDetailAPIView.as_view(), name='detail_watch'),
    path('detail-pc/<pk>', ExpertisePcDetailAPIView.as_view(), name='detail_pc'),
]