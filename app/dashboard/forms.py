from django import forms


from dashboard.models import Transaction


class UpdateTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            "date",
            "quantity",
            "currency",
            "price"
        ]