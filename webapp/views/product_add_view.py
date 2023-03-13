from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import ProductForm
from webapp.models import Product


class ProductCreateView(CreateView):
    template_name = "product_add.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse("product_view", kwargs={"pk": self.object.pk})
