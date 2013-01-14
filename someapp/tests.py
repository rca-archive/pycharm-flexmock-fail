from django.test import TestCase

from flexmock import flexmock

from someapp.views import MyView


class FlexMockTestCase(TestCase):
    def test_this_should_fail(self):
        flexmock(MyView).should_receive('post').once()
