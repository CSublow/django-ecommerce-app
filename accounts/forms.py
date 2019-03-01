from django import forms
from django.contrib.auth.models import User # Import the user module provided by Django
from django.contrib.auth.forms import UserCreationForm # This will give usernames and emails, all you need to do is extend it to work with passwords
from django.core.exceptions import ValidationError # Form validation

class UserLoginForm(forms.Form): # UserLoginForm inherits from forms.Form
    """ Form to be used to log in users """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) # The password input widget will render a textbox but one suitable for passwords
    
class UserRegistrationForm(UserCreationForm): # The class inherits from UserCreationForm
    """ Form used to register a new user """
    password1 = forms.CharField(label = "Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Password Confirmation", widget = forms.PasswordInput)
    
    class Meta: # Meta is an inner class
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        
    # Form Validation
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        # User a filter to check that no duplicate email addresses can be registered
        if User.objects.filter(email = email).exclude(username = username):
            raise forms.ValidationError(u'There is already an account associated with this email address')
        return email
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        # Check to see the fields aren't empty
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
            
        # Check to ensure password and confirm password inputs are equal
        if password1 != password2:
            raise ValidationError("Passwords must match")
            
        return password2
        
    