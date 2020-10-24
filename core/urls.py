from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('', views.NoteViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('account/register', views.UserCreate.as_view({"post":"create"})),
    path('account/login', obtain_auth_token, name='obtain-token')
]
