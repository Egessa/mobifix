from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    firstname   = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'type':'text',
                                                                            'class':'form-control',
                                                                            'id':'fname',
                                                                            }))
    lastname    = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'type':'text',
                                                                            'class':'form-control',
                                                                            'id':'lname',}))
    number      = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'type':'tel',
                                                                            'class':'form-control',
                                                                            'id':'telephone',}))
    email       = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'type':'email',
                                                                            'class':'form-control',
                                                                            'id':'email',}))
    message     = forms.CharField(max_length=200,widget=forms.Textarea(attrs={'name':'message',
                                                                            'class':'form-control',
                                                                            'id':'message',
                                                                            'rows':5,
                                                                            'col':20,
                                                                            'placeholder':'Talk to us...'}))

    class Meta:
        model= Contact
        fields=('firstname','lastname','number','email','message')
