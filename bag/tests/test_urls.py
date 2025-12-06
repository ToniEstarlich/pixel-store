from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bag import views


class BagUrlsTestCase(SimpleTestCase):

    def test_view_bag_url_resolves(self):
        url = reverse("view_bag")
        self.assertEqual(resolve(url).func, views.view_bag)

    def test_add_to_bag_url_resolves(self):
        url = reverse("add_to_bag", args=[1])
        self.assertEqual(resolve(url).func, views.add_to_bag)

    def test_remove_from_bag_url_resolves(self):
        url = reverse("remove_from_bag", args=["1"])
        self.assertEqual(resolve(url).func, views.remove_from_bag)

    def test_clear_bag_url_resolves(self):
        url = reverse("clear_bag")
        self.assertEqual(resolve(url).func, views.clear_bag)
