from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

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

    # test for profile creation upon user creation
    def test_profile_created(self):
        new_user = create_user(
            first_name='New',
            last_name='User',
            username='NewUser2',
            email='newUser2@gmail.com',
            password='abc123!'
        )

        new_user_profile = Profile.objects.get(user=new_user)

        # verify that a new profile has been created
        self.assertTrue(Profile.objects.filter(user=new_user).exists())

        # verify that that the new profile has a profile photo
        self.assertTrue(hasattr(new_user_profile,'profile_photo'))

        # verify that the new profile has the same informaiton as the user
        attributes = ['first_name', 'last_name', 'username', 'email', 'password']
        for attribute in attributes:
            self.assertEqual(getattr(new_user_profile.user, attribute), getattr(new_user, attribute))
    
    # test that a profile is deleted when a user is deleted
    def test_profile_deleted(self):
        new_user = create_user(
            first_name='New',
            last_name='User',
            username='NewUser3',
            email='newUser3@gmail.com',
            password='abc123!'
        )

        # verify that a new profile has been created
        self.assertTrue(Profile.objects.filter(user=new_user).exists())


        # verify that the associated profile is deleted when the user is deleted
        new_user.delete()
        self.assertFalse(Profile.objects.filter(user=new_user).exists())