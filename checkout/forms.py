from django import forms # Django has a built in way of using forms
from .models import Order

# Stripe deals with the encryption of the credit card details using its Javascript
class MakePaymentForm(forms.Form):
    # Month choices needed for valid from/expiry date for card payments
    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]
    
    # Stripe requires certain fields
    # required=false is used here so that the plaintext of this information is not transmitted through the browser
    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code(CVV)', required=False)
    # The choice field here uses the MONTH_CHOICES you defined above
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)
    # Stripe requires an id. Although it's being added to the form the user won't actually see this
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
# In addition to a payment form you also need an order form
# This uses the Order model that you created in models.py
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county_or_province')
    