from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from webapp.forms import ProductForm
from webapp.models import Product


class ProductDetail(DetailView):
    template_name = "product_view.html"
    model = Product

    def get_queryset(self):
        return Product.objects.all()


class ProductDeleteView(DeleteView):
    template_name = "product_confirm_delete.html"
    model = Product
    success_url = reverse_lazy("products")


class ProductUpdateView(UpdateView):
    template_name = "product_edit_view.html"
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse("product_view", kwargs={"pk": self.object.pk})
