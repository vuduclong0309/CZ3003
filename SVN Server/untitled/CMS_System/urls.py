from django.conf.urls import url,include
from CMS_System import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import WeatherViewSet

router = routers.DefaultRouter()
router.register(r'weather',WeatherViewSet)
#router.register(r'weather',WeatherAPI)

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^',include(router.urls)),
    #url(r'^weather',views.WeatherAPI.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)