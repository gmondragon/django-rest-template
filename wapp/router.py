from rest_framework import routers

from users import views as users

router = routers.DefaultRouter()
router.register('users', users.UserViewSet, basename='users')

urlpatterns = router.urls
