from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nom")
    email = forms.EmailField(label="Email")
    subject = forms.CharField(max_length=200, label="Sujet")
    message = forms.CharField(widget=forms.Textarea, label="Message")
