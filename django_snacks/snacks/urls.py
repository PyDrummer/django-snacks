from django.urls import path
from .views import HomePageView, AboutView

urlpatterns = [
    # The '' home route, from Homepageview with a readable name of 'home'
    # Must have a comma between the paths
    path('', HomePageView.as_view(), name = 'home'),
    path('about', AboutView.as_view(), name = 'about')
]
