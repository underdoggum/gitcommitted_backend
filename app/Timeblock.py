"""Timeblock Model."""

from masoniteorm.models import Model
# from masoniteorm.relationships import has_many


class Timeblock(Model):
    __table__ = "timeblocks"
    # @has_many("id", "timeblock_id")
    # def reminders(self):
    #     from app.Reminder import Reminder
    #     return Reminder