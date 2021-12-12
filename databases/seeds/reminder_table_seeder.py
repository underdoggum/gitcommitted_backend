"""ReminderTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Reminder import Reminder


class ReminderTableSeeder(Seeder):
    def run(self):
        # Re-seed in case data is compromised
        Reminder.delete()
        Reminder.create({ "text": "Do the thing" })
        Reminder.create({ "text": "Call that person" })
        Reminder.create({ "text": "Sketch out that other thing" })
        Reminder.create({ "text": "url: https://google.com" })
