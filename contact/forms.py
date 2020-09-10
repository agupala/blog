from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Name", required=True, widget=forms.TextInput(
        attrs= {
            'class':'form-control',
            'placeholder': 'Name'
        }
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
        }
    ), min_length=3, max_length=100)
    phone = forms.CharField(label="Phone", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Phone number',
        }
    ), min_length=3, max_length=100)
    content = forms.CharField(label="Message", required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Message',
        }
    ), min_length=3, max_length=1000)