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
            ## Field to track which user created the timeblock
            table.integer("user_id")
            ## Defining the field as a foreign key
            table.foreign("user_id").references("id").on("users")
            ## Create the field that will be the foreign key
            # table.integer("timeblock_id")
            ## Foreign key field tracking id of related owner
            # table.foreign("timeblock_id").references("id").on("timeblocks")
            
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("timeblocks")
