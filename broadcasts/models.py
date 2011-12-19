from django.db import models

from broadcasts.managers import BroadcastManager


class BroadcastMessage(models.Model):
    """
    A broadcast message to be displayed on the site.
    """
    message = models.CharField(max_length=140)
    start_time = models.DateTimeField(null=True, blank=True,
            help_text="""Optional, used to start showing a message in the
            future""")
    end_time = models.DateTimeField(help_text="""When this message should
            expire""")
    is_published = models.BooleanField(default=True, verbose_name="Published?")
    objects = BroadcastManager()

    class Meta:
        ordering = ["-end_time"]

    def __unicode__(self):
        return u"%s" % self.message[:15]
