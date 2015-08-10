from django.test import TestCase

from .models import HikeItUser

class UserTestCase(TestCase):
    def test_create_user(self):
        user = HikeItUser.objects.create(email="test@foo.bar", password="kasjdfkljaskdf", first_name="Foo", last_name="Bar")
        user.save()
        self.assertEquals(user.first_name, "Foo")