from datetime import datetime
from datetime import timedelta

from django.test import TestCase

from broadcasts.models import BroadcastMessage


class BroadcastManagerTest(TestCase):
    """
    This test case ensures that the manager methods return the correct
    broadcast or broadcasts based on the start time, end time, and published
    status of the available messages.
    """

    def setUp(self):
        """
        The test case should have one broadcast message for each combination of
        setting, i.e. current, past, future, published, with or without start
        dates
        """
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        anteayer = today - timedelta(days=2)
        tomorrow = today + timedelta(days=1)
        morefuture = today + timedelta(days=2)

        self.pub_expired = BroadcastMessage.objects.create(
                message="Expired messsage",
                end_time=yesterday,
                )
        self.pub_current_no_start = BroadcastMessage.objects.create(
                message="Current, but no start",
                end_time=morefuture,
                )
        self.pub_current_start_yesterday = BroadcastMessage.objects.create(
                message="Current, started yesterday",
                start_time=yesterday,
                end_time=tomorrow,
                )
        self.pub_current_ends_later = BroadcastMessage.objects.create(
                message="Current, ends later",
                start_time=yesterday,
                end_time=morefuture,
                )


    def test_past_broadcasts(self):
        """Ensure that expired broadcasts are not returned"""
        self.assertEqual(len(BroadcastMessage.objects.all()), 4)
        self.assertEqual(len(BroadcastMessage.objects.current()), 3)

    def test_latest_broadcast(self):
        """Ensure that the latest broadcast is soonest to expire, current"""
        self.assertEqual(self.pub_current_start_yesterday,
                BroadcastMessage.objects.latest())
