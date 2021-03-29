from rest_framework.routers import SimpleRouter
from rentalsystem.accounts.views import ProfileViewSet, LandlordProfileViewSet

router = SimpleRouter()
router.register("accounts", ProfileViewSet)
router.register("landlord", LandlordProfileViewSet)

urlpatterns = router.urls
