from django.urls import path, include
from rest_framework.routers import SimpleRouter
from core.views import SignUpView

# from rest_framework_nested import routers

# signup_router = SimpleRouter()
# signup_router.register('signup', SignUpView, basename="signup")

# comments_router = routers.NestedSimpleRouter(ads_router, "ads", lookup="ad")
# comments_router.register("comments", CommentViewSet, basename="comments")


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
]


