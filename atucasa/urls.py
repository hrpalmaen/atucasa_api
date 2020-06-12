''' File for routes in aplication '''

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'product', ProductView)
router.register(r'user', UserView)
router.register(r'branch', BranchView)
router.register(r'city', CityView)
router.register(r'store', StoreView)
router.register(r'category_store', CategoryStoreView)
router.register(r'category_product', CategoryProductView)

urlpatterns = [
    path('auth/', AuthView.as_view(), name='login'),
    path('', include(router.urls)),
    # path('restorePassword/', RestorePasswordView.as_view(), name='searchUser')
]