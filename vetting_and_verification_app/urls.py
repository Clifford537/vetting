

from django.urls import path
from .views import (
    ClientListCreateView, ServiceProviderListCreateView,
    ExperienceListCreateView, SkillListCreateView #VettingView
)

urlpatterns = [
    #path('api/vetting/', VettingView.as_view(), name='vetting_view'),
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('service_providers/', ServiceProviderListCreateView.as_view(), name='service-provider-list-create'),
    path('experiences/', ExperienceListCreateView.as_view(), name='experience-list-create'),
    path('skills/', SkillListCreateView.as_view(), name='skill-list-create'),
]

