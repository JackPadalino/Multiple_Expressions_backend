from django.test import TestCase
from django.contrib.auth.models import User
# from .models import Profile

# Create your tests here.
def create_user(first_name,last_name,username,email,password):
    return User.objects.create(first_name=first_name,last_name=last_name,username=username,email=email,password=password)

class UserTests(TestCase):
    # test for creation of a new user
    def test_user_created(self):
        new_user = create_user(
            first_name='New',
            last_name='User',
            username='NewUser1',
            email='newUser1@gmail.com',
            password='abc123!'
        )

        saved_user = User.objects.get(username="NewUser1")
        
        attributes = ['first_name','last_name','username','email','password']
        # verify that the new user has all fields
        for attribute in attributes:
            self.assertTrue(hasattr(new_user,attribute))
            self.assertEqual(getattr(new_user, attribute), getattr(saved_user, attribute))
            