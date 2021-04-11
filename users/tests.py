# Django Utility imports
from django.test import TestCase
from django.contrib.auth import get_user_model

# Testing class for User account creation testing
class UserAccountTests(TestCase):
    '''
    This class tests the creation of simple user account as well as superuser account creation.
    '''
    def test_new_superuser(self):
        '''
        Tests super user account creation.
        '''
        # getting the model instance for User model
        db = get_user_model()
        
        # creating a super user account
        super_user = db.objects.create_superuser(
            'testuser@django.com', 'username', 'first_name', 'password'
        )
        
        # Testing asserts for superuser account information.
        self.assertEqual(super_user.email, 'testuser@django.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'first_name')
        self.assertEqual(str(super_user), 'username')
        
        # Testing the statuses for superuser
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)

        # Testing the error handlers for wrong superuser status
        with self.assertRaises(ValueError):
            
            db.objects.create_superuser(
                email='testuser@django.com',
                user_name='username',
                first_name='first_name',
                password='password',
                is_superuser=False
            )

        # Testing the error handlers for wrong staff status
        with self.assertRaises(ValueError):
            
            db.objects.create_superuser(
                email='testuser@django.com',
                user_name='username',
                first_name='first_name',
                password='password',
                is_staff=False
            )

        # Testing the error handlers for empty email address
        with self.assertRaises(ValueError):
            
            db.objects.create_superuser(
                email='',
                user_name='username',
                first_name='first_name',
                password='password',
                is_staff=False
            )
    
    def test_new_user(self):
        '''
        Tests a simple user account creation
        '''
        db = get_user_model()

        # Creating the simple user account
        user = db.objects.create_user(
            'testuser1@django.com', 'username', 'first_name', 'password' 
        )

        # Testing the asserts for user account info
        self.assertEqual(user.email, 'testuser1@django.com')
        self.assertEqual(user.user_name, 'username')
        self.assertEqual(user.first_name, 'first_name')
        self.assertEqual(str(user), 'username')

        # Testing the status for simple user account
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)

        # Testing the error handlers for empty email address
        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='',
                user_name='username',
                first_name='first_name',
                password='password',
            )