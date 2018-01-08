from django import forms

from .models import *

class CashierForm(forms.ModelForm):
    class Meta:
        model = Fees_Accounts
        fields = [
            "FA_name",
            "amount"
        ]