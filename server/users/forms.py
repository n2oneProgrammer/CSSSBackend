from django import forms
from django.contrib.auth import (authenticate, get_user_model)  

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Nie istnieje taki użytkownik!')
            if not user.check_password(password):
                raise forms.ValidationError('Niepoprawne hasło!')
            if not user.is_activate:
                raise forms.ValidationError('Użytkownik jest nieaktywny!')

        return super(UserLoginForm, self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm):

    username = forms.CharField(label="Nickname")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label='Hasło')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Powtórz hasło')

    class Meta:
        model = User
        fields=['username','email','password','password2']

    def clean_email_password(self):

        email = self.cleaned_data.get('email')
        emailQuery = User.objects.filter(email=email)
        if(emailQuery.exists()):
            raise forms.ValidationError('Taki email już istnieje w naszej bazie!')
        return email

    def clean_password(self):
        
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Hasła nie są identyczne!')
        return password