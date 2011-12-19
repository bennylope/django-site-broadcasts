from datetime import datetime

from django.db import models
from django.db.models import Q


class BroadcastManager(models.Manager):
    """
    Manager class to show only active broadcast messages
    """

    def active(self):
        """Return only active messages"""
        return super(BroadcastManager, self).filter(is_published=True)

    def current(self):
        """Return only current and active messages"""
        return self.active().filter(end_time__gte=datetime.now()).filter(
            Q(Q(start_time__lte=datetime.now()) | Q(start_time=None)))

    def latest(self):
        """Return the broadcast message to display"""
        try:
            return self.current().order_by("end_time")[0]
        except IndexError:
            return None

