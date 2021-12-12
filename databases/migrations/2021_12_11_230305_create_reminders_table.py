"""CreateRemindersTable Migration."""

from masoniteorm.migrations import Migration


class CreateRemindersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("reminders") as table:
            table.increments("id")
            table.string("text")
            table.integer("category")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("reminders")
