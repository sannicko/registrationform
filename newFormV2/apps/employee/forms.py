from django import forms

class SubmitForm(forms.Form):
    #your_name = forms.CharField(label='Your name', max_length=100)
    receive_newsletter = forms.BooleanField()