from django import forms

from .models import Product


# class ProductForm(forms.Form):
#     title = forms.CharField()

class ProductModelForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = Product
        fields = [
            "title",
            "desc",
            "price"
        ]

    # custom data validation
    def clean_title(self):
        data = self.cleaned_data.get("title")
        if len(data) < 2:
            raise forms.ValidationError("The title is not long enough.")
        return data
