from django.urls import path
from .views import HomePageView
from .views import AboutPageView
#O simplemente "from .views import HomePageView, AboutPageView"

urlpatterns = [
    path("", HomePageView.as_view(), name ="home"),
    path("about/", AboutPageView.as_view(), name ="About"),
]