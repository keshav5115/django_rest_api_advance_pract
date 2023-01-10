from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('product',views.ProductModelVW,basename='product')


urlpatterns=[
    path('cust/',views.CustomerListAV.as_view(),name='cust'),
    path('cone/<int:pk>/',views.CustomerViewDetail.as_view(),name='cone'),
    path('',include(router.urls)),
    # path('product/',views.ProductListAV.as_view(),name='product'),
    # path('product/<int:pk>/',views.ProductViewDetail.as_view(),name='prduct_one'),

    path('product/<int:pk>/review-create',views.ReviewCreateView.as_view(),name='review_create'),
    path('product/<int:pk>/review',views.ReviewListMixin.as_view(),name='review'),
    path('product/review/<int:pk>',views.ReviewDetailView.as_view(),name='review_one'),

    # path('review/',views.ReviewListMixin.as_view(),name='review'),
    # path('review_one/<int:pk>/',views.ReviewDetailView.as_view(),name='review_one'),
]