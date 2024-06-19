from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contact.models import Contact

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    'class': 'classe-a',
                    'placeholder': 'Escreva neste campo',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de Ajuda'
    )
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'    
            }    
        )        
    )
    
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
        )
        
    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError(
                    'O primeiro nome não pode ser igual ao segundo!',
                    code='invalid'    
                )
                       
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Este campo não pode ser ABC!',
                    code='invalid'    
                )        
        )
        
        return first_name
    
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,    
    )
    
    last_name = forms.CharField(
        required=True,
        min_length=3,    
    )
    
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Já existe um usuário com esse e-mail!',
                    code='invalid'    
                )     
            )               

        return email   