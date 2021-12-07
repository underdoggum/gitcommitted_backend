""" A TimeblockController Module """

from masonite.controllers import Controller
from masonite.request import Request
from app.Timeblock import Timeblock


class TimeblockController(Controller):
    """
    This controller is for a Timeblock schema, which contains many Reminder items
    """

    def __init__(self, request:Request):
        self.request = request

    def show(self):
        id = self.request.param("id")
        return Timeblock.where("id", id).get()

    def index(self):
        return Timeblock.all()

    def create(self):
        title = self.request.input("title")
        timeblock = Timeblock.create({ "title": title })
        return timeblock

    def update(self):
        id = self.request.param("id")
        title = self.request.input("title")
        Timeblock.where("id", id).update({ "title": title })
        return Timeblock.where("id", id).get()

    def destroy(self):
        id = self.request.param("id")
        timeblock = Timeblock.where("id", id).get()
        Timeblock.where("id", id).delete()
        return timeblock
