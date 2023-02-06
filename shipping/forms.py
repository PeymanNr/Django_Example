from django import forms
from django.core.exceptions import ValidationError

from shipping.models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['user' , 'city', 'zipcode', 'address', 'number']
        exclude = ['user']
        # feilds = '__all__'

    def clean_zipcode(self):
        zipcode = self.cleaned_data['zipcode']
        if len(zipcode) != 16:
            raise ValidationError('Lenght is not 16')

        return zipcode