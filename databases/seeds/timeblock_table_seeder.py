"""TimeblockTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Timeblock import Timeblock


class TimeblockTableSeeder(Seeder):
    def run(self):
        # Re-seed in case data is compromised
        Timeblock.delete()
        Timeblock.create({ "title": "Projects/New Tech" })
        Timeblock.create({ "title": "Networking" })
        Timeblock.create({ "title": "Coding Challenges" })
        Timeblock.create({ "title": "Job Applications" })
