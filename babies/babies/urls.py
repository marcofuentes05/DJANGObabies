from django.contrib import admin
from django.urls import path
from babyevents.views import ParentViewSet, BabyViewSet, EventsViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from rest_framework_jwt.views import (
    obtain_jwt_token,
    refresh_jwt_token
)


router = DefaultRouter()
router.register(r'parent', ParentViewSet)
router.register(r'baby', BabyViewSet)
router.register(r'events', EventsViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/token-auth/', obtain_jwt_token),
    url(r'^api/v1/token-refresh/', refresh_jwt_token),
]
