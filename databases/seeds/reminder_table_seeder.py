"""ReminderTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Reminder import Reminder


class ReminderTableSeeder(Seeder):
    def run(self):
        # Re-seed in case data is compromised
        Reminder.delete()
        Reminder.create({ "text": "Sketch out that wireframe", "category": 1 })
        Reminder.create({ "text": "Learn that new front-end framework", "category": 1 })
        Reminder.create({ "text": "Send out connection request for people at that company", "category": 2 })
        Reminder.create({ "text": "Message that person on LinkedIn", "category": 2 })
        Reminder.create({ "text": "Practice on the CoderPad site", "category": 3 })
        Reminder.create({ "text": "Learn new techniques for object manipulation", "category": 3 })
        Reminder.create({ "text": "Update your master resume", "category": 4 })
        Reminder.create({ "text": "Apply to that hip new company", "category": 4 })


