from django.urls import path

from webapp.views.cart_view import CartView
from webapp.views.product_view import (
    ProductDetail,
    ProductUpdateView,
    ProductDeleteView, ProductCreateView,
)

from webapp.views.products_view import ProductView, ProductRedirectView

urlpatterns = [
    path("", ProductView.as_view(), name="products"),
    path("products", ProductRedirectView.as_view(), name="products_redirect"),
    path("products/add", ProductCreateView.as_view(), name="product_add"),
    path("product/<int:pk>", ProductDetail.as_view(), name="product_view"),
    path(
        "product/delete/<int:pk>",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path(
        "product/<int:pk>/confirm_delete/",
        ProductDeleteView.as_view(),
        name="confirm_delete",
    ),
    path(
        "products/<int:pk>/edit",
        ProductUpdateView.as_view(),
        name="product_edit",
    ),
    path("cart/", CartView.as_view(), name="cart_view"),
]
