from django.urls import path
from expertise_forms.api.views import (
                            ExpertiseTVCreateAPIView,
                        )

app_name = 'expertise_forms'


urlpatterns = [
    path('create', ExpertiseTVCreateAPIView.as_view(), name='create'),
]