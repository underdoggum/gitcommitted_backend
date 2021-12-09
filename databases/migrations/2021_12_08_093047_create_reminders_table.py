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
            ## Field to track which user created the item
            table.integer("user_id")
            ## Defining the field as a foreign key
            table.foreign("user_id").references("id").on("users")
            ## Create the field that will be the foreign key
            table.integer("timeblock_id")
            ## Foreign key field tracking id of related timeblock
            table.foreign("timeblock_id").references("id").on("timeblocks")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("reminders")
