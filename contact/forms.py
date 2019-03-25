from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=40, required=False, help_text="Your Name")
    email = forms.EmailField(required=True, help_text="johndoe@example.com")
    comment = forms.CharField(required=True, widget=forms.Textarea)