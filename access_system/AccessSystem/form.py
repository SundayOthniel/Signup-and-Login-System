from django.forms import ModelForm
from .models import SignUp
from django.core.exceptions import ValidationError


class SignUpForm(ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'

    def clean_number(self):
        number = self.cleaned_data['number']
        if '+' not in number:
            raise ValidationError(number + ' does not start with + and add your country code')
            
        special_character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`!@#$%^&*()_-=[{|"}]:;?>/<,'
        for char in special_character:
            if char in number:
                raise ValidationError('Special characters are not allowed.')  
        return number
