from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required # Allows you to use the login_required decorator, checking that a user is logged in before continuing code execution
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm

# Create your views here.
def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')
    
@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request) # Request contains the user object
    messages.success(request, "You have been logged out successfully")
    return redirect(reverse('index')) # reverse allows you to pass in the name of a url as opposed to a view
    
def login(request):
    """ Return the login page """
    # If the user clicks 'login' when they are already logged in, take them back to the index page
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST) # The login form will be created with the data actually posted in from the form
        # You also need to check that data is valid
        if login_form.is_valid():
            # The below line authenticates the user and checks if the user has actually provided a correct username and password, although it won't on its own log the user in
            user = auth.authenticate(username = request.POST['username'], # Retrieve the username from the POST dictionary
                                     password = request.POST['password'])
            
            # The authenticate will return a user object
            if user: # If there is a user object (i.e the authentication was successful)
                auth.login(user=user, request=request) # Log them in
                messages.success(request, "You have logged in successfully") # Provide feedback in the event of a successful log in
                return redirect(reverse('index')) # Take the user back to the home page
            else:
                login_form.add_error(None, "Invalid login") # 'None' means the error will just display on the form
    else:
        login_form = UserLoginForm() # Else just create an empty object
    # login_form = UserLoginForm()# Create an instance of the login form
    return render(request, 'login.html', {"login_form": login_form})
    
def registration(request):
    """ Render the registration page """
    # If a user is already logged in, the Register button will just take them back to index.html
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == 'POST':
        # Instantiate the registration form using the values contained within the post method
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save() # The model has already been specified on the Meta class in forms.py
        
            # Once we have created user we log user in
            user = auth.authenticate(username = request.POST['username'],
                                     password = request.POST['password1'])
                                     
            if user: # If/when our user is authenticated
                auth.login(user = user, request = request)
                messages.success(request, "You have been successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
                                     
    else: # Else the request will be a get method
        registration_form = UserRegistrationForm() # Instantiate an empty registration form
        
    return render(request, 'registration.html', 
    {'registration_form': registration_form})
    
def user_profile(request):
    """ The user's profile page """
    user = User.objects.get(email = request.user.email) # Retrieve the user from the database
    return render(request, 'profile.html', {'profile': user})
    