import string
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Sum

from webapp.models import Product, Cart


def eng_letters_validator(title):
    # проверяем требование на отсутствие кириллицы в поле 'tltle'
    if not all(abc in string.printable for abc in title):
        raise ValidationError("You need to fill in only English letters")
    return title


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        label="Заголовок",
        validators=(eng_letters_validator,),
    )

    class Meta:
        model = Product
        fields = (
            "title",
            "description",
            "category",
            "price",
            "image",
            "balance",
        )

        labels = {
            "title": "Заголовок",
            "description": "Описание",
            "category": "Категория",
            "price": "Цена",
            "image": "Ссылка на изображение",
            "balance": "Остаток",
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 2:
            raise ValidationError("Title must be longer than 2 characters")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) < 2:
            raise ValidationError(
                "Description must be longer than 2 characters"
            )
        return description

    def clean_balance(self):
        balance = self.cleaned_data.get("balance")
        if balance < 0:
            raise ValidationError("The balance of goods cannot be less than 0")
        return balance


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label="Search")


class CartForm(forms.ModelForm):

    class Meta:
        model = Cart
        fields = (
            "balance",
        )

        labels = {
            "balance": "Количество",
        }