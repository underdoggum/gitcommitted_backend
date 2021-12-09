"""A ReminderTimeblockController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Reminder import Reminder
from app.Timeblock import Timeblock


class ReminderTimeblockController(Controller):
    """ReminderTimeblockController Controller Class."""

    def __init__(self, request: Request):
        self.request = request

    ## Index
    def get_user_timeblocks(self):
        return self.request.user().timeblocks

    def get_user_reminders(self):
        return self.request.user().reminders

    ## Create
    def create_timeblock(self):
        user = self.request.user()
        title = self.request.input("title")
        print(user)
        timeblock = Timeblock.create(title=title, user_id=user["id"])
        return timeblock

    def create_reminder(self):
        user = self.request.user()
        text = self.request.input("text")
        timeblock_id = self.request.input("timeblock_id")
        reminder = Reminder.create(text=text, timeblock_id=timeblock_id, user_id=user.id)
        return reminder

    ## Update
    

    ## Destroy
    

    def show(self, view: View):
        pass
