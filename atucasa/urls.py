''' File for routes in aplication '''

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'product', ProductView, basename='Product')
router.register(r'user', UserView)
router.register(r'branch', BranchView)
router.register(r'city', CityView)
router.register(r'store', StoreView, basename="Store")
router.register(r'category_store', CategoryStoreView)
router.register(r'category_product', CategoryProductView)
router.register(r'groups_user', GroupView)

urlpatterns = [
    path('auth/', AuthView.as_view(), name='login'),
    path('', include(router.urls)),
    # path('restorePassword/', RestorePasswordView.as_view(), name='searchUser')
]