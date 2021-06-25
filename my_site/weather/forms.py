from django import forms

class CityForm(forms.Form):
    City = forms.CharField(widget=forms.TextInput(attrs={'id': 'fild_weather', 'placeholder': 'Введите город'}), max_length=30, label='')
