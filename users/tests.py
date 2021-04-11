from django.test import TestCase
from django.contrib.auth import get_user_model

class UserAccountTests(TestCase):

    def test_new_superuser(self):
        db = get_user_model()
        
        super_user = db.objects.create_superuser(
            'testuser@django.com', 'username', 'first_name', 'password'
        )

        self.assertEqual(super_user.email, 'testuser@django.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'first_name')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_active)
        self.assertEqual(str(super_user), 'username')

        with self.assertRaises(ValueError):
            
            db.objects.create_superuser(
                email='testuser@django.com',
                user_name='username',
                first_name='first_name',
                password='password',
                is_superuser=False
            )

        with self.assertRaises(ValueError):
            
            db.objects.create_superuser(
                email='testuser@django.com',
                user_name='username',
                first_name='first_name',
                password='password',
                is_staff=False
            )

        with self.assertRaises(ValueError):
            
            db.objects.create_superuser(
                email='',
                user_name='username',
                first_name='first_name',
                password='password',
                is_staff=False
            )
    
    def test_new_user(self):
        db = get_user_model()

        user = db.objects.create_user(
            'testuser1@django.com', 'username', 'first_name', 'password' 
        )

        self.assertEqual(user.email, 'testuser1@django.com')
        self.assertEqual(user.user_name, 'username')
        self.assertEqual(user.first_name, 'first_name')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_active)
        self.assertEqual(str(user), 'username')

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='',
                user_name='username',
                first_name='first_name',
                password='password',
            )