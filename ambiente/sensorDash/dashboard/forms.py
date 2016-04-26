from django import forms


class DateRangeForm(forms.Form):
    initialDate = forms.DateField()
    initialTime = forms.TimeField()
    finalDate = forms.DateField()
    finalTime = forms.TimeField()
