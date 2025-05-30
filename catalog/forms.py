from django.forms import ModelForm
from django.core.exceptions import ValidationError

from .models import Product, Category

spam_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        #exclude = ('name',)
        fields = '__all__'

    def clean(self):
        name = self.cleaned_data['name']
        description = self.cleaned_data['description']
        if set(name.lower().split())&set(spam_words) or set(description.lower().split())&set(spam_words):
            message = f'Спам-слова запрещено использовать, необходимо убрать:\n {' '.join(set(name.lower().split())&set(spam_words))} {' '.join(set(description.lower().split())&set(spam_words))}!!!'
            raise ValidationError(message)



