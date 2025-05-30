from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError

from .models import Product, Category

spam_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixim:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            fild.widget.attrs['class'] = "form-control"

class ProductForm(StyleFormMixim, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at','updated_at')

    def clean(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        if set(name.lower().split()) & set(spam_words) or set(description.lower().split()) & set(spam_words):
            message = f'Спам-слова запрещено использовать, необходимо убрать:\n {' '.join(set(name.lower().split()) & set(spam_words))} {' '.join(set(description.lower().split()) & set(spam_words))}!!!'
            raise ValidationError(message)

    def clean_price(self):
        price = self.cleaned_data['price']
        if int(price) < 0:
            raise ValidationError("Недопустима отрицательная цена!")
        return price
