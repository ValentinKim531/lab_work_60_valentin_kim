from django.db.models import Sum, Count, F
from django.views.generic import ListView

from webapp.models import Cart, Product


class CartView(ListView):
    model = Cart
    template_name = "products_in_cart.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        total = Cart.objects.all
        context['total'] = total
        return context




