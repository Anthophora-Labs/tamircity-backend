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
]