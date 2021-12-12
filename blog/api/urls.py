from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from blog.api.views import PostViewSet, UserDetail, TagViewSet

from django.urls import path, include

from rest_framework.authtoken import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("tags", TagViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    path("users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
    path("auth/", include("rest_framework.urls")),
    path("token-auth/", views.obtain_auth_token),
    path("", include(router.urls)),
]
