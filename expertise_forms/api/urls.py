from django.urls import path
from expertise_forms.api.views import (
                            ExpertiseTVCreateAPIView,
                            ExpertiseWatchListAPIView,
                        )

app_name = 'expertise_forms'


urlpatterns = [
    path('expertise-tv', ExpertiseTVCreateAPIView.as_view(), name='create_expertise_tv'),
    path('expertise-watch', ExpertiseWatchListAPIView.as_view(), name='create_expertise_watch'),
]