"""CreateTimeblocksTable Migration."""

from masoniteorm.migrations import Migration


class CreateTimeblocksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("timeblocks") as table:
            table.increments("id")
            table.string("title")
            
            # ## Create the field that will be the foreign key
            # table.integer("timeblock_id")
            # ## Foreign Key Field tracking id of related owner
            # table.foreign("timeblock_id").references("id").on("timeblocks")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("timeblocks")
