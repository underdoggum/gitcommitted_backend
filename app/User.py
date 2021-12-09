"""User Model."""

from masoniteorm.models import Model
from masoniteorm.relationships import has_many


class User(Model):
    """User Model."""

    __fillable__ = ["username", "email", "password"]

    __auth__ = "username"

    ## Establish that users can have many reminders
    @has_many("id", "user_id")
    def reminders(self):
        from app.Reminder import Reminder
        return Reminder

    ## Establish that users can have many timeblocks
    @has_many("id", "user_id")
    def timeblocks(self):
        from app.Timeblock import Timeblock
        return Timeblock
