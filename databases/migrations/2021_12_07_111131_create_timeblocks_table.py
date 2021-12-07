"""CreateTimeblocksTable Migration."""

from masoniteorm.migrations import Migration
# from masoniteorm.relationships import has_many


class CreateTimeblocksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("timeblocks") as table:
            table.increments("id")
            table.string("title")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("timeblocks")
