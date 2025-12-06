from django.test import TestCase
from django.contrib.auth.models import User
from users.models import UserProfile


class UserProfileModelTests(TestCase):

    def test_userprofile_str_returns_username(self):

        user = User.objects.create_user(username="john")
        profile = UserProfile.objects.create(user=user)
        self.assertEqual(str(profile), "john")
