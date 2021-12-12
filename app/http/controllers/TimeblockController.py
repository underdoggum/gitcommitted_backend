""" A TimeblockController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Timeblock import Timeblock
from app.Reminder import Reminder


class TimeblockController(Controller):
    def __init__(self, request:Request):
        self.request = request

    ## for Timeblocks
    def showTimeblock(self):
        id = self.request.param("id")
        return Timeblock.where("id", id).get()

    def indexTimeblock(self):
        return Timeblock.all()

    def createTimeblock(self):
        title = self.request.input("title")
        # ## for Reminder one-to-many relationship
        # timeblock_id = self.request.input("timeblock_id")
        timeblock = Timeblock.create({ "title": title })
        return timeblock

    def updateTimeblock(self):
        id = self.request.param("id")
        title = self.request.input("title")
        Timeblock.where("id", id).update({ "title": title })
        return Timeblock.where("id", id).get()

    # def destroyTimeblock(self):
    #     id = self.request.param("id")
    #     timeblock = Timeblock.where("id", id).get()
    #     Timeblock.where("id", id).delete()
    #     return timeblock


    ## for Reminders
    def showReminder(self):
        id = self.request.param("id")
        return Reminder.where("id", id).get()

    def indexReminder(self):
        return Reminder.all()

    def createReminder(self):
        text = self.request.input("text")
        category = self.request.input("category")
        reminder = Reminder.create({ "text": text, "category": category })
        return reminder

    def updateReminder(self):
        id = self.request.param("id")
        text = self.request.input("text")
        category = self.request.input("category")
        Reminder.where("id", id).update({ "text": text, "category": category })
        return Reminder.where("id", id).get()

    def destroyReminder(self):
        id = self.request.param("id")
        reminder = Reminder.where("id", id).get()
        Reminder.where("id", id).delete()
        return reminder