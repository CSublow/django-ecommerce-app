from django.contrib.auth.models import User

class EmailAuth:
    """ Authenticate a user by an exact match on the email and password """
    
    def authenticate(self, username=None, password=None): # username and password are set to none by default
        """ Get an instance of 'User' based off the email and verify the password """
        try:
            user = User.objects.get(email=username) # The reason why this is set to username is because that is what the name of the form element is
            
            if user.check_password(password): # Return user if the password is correct
                return user
            return None
        except User.DoesNotExist:
            return None
            
    def get_user(self, user_id):
        """ Used by the Django authentication system to retrieve a user instance """
        try:
            user = User.objects.get(pk=user_id)
            
            if user.is_active:
                return user
            return None
            
        except User.DoesNotExist:
            return None