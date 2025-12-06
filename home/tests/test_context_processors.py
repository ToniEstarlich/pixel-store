from django.test import TestCase, RequestFactory
from home.context_processors import timestamp


class ContextProcessorTests(TestCase):

    def test_timestamp_processor_returns_timestamp(self):

        # the context processor return int
        factory = RequestFactory()
        request = factory.get("/")
        context = timestamp(request)
        self.assertIn("timestamp", context)
        self.assertIsInstance(context["timestamp"], int)
