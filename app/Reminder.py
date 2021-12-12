"""Reminder Model."""

from masoniteorm.models import Model


class Reminder(Model):
    __table__ = "reminders"