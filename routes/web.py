"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),

    RouteGroup([
        Post("/login", "AuthController@login").name("login"),
        Post("/signup", "AuthController@signup").name("signup"),
        Post("/logout", "AuthController@logout").name("logout")
    ], prefix="/auth"),

    RouteGroup([
        Get("/timeblocks", "ReminderTimeblockController@get_user_timeblocks").name("get_timeblocks"),
        Get("/reminders", "ReminderTimeblockController@get_user_reminders").name("get_reminders"),
        Post("/timeblocks", "ReminderTimeblockController@create_timeblock").name("create_timeblock"),
        Post("/reminders", "ReminderTimeblockController@create_reminder").name("create_reminder")
    ], prefix="/timeblockreminders", middleware=["auth"])
    
        # Get("/", "TimeblockController@index").name("index"),
        # Get("/@id", "TimeblockController@show").name("show"),
        # Post("/", "TimeblockController@create").name("create"),
        # Put("/@id", "TimeblockController@update").name("update"),
        # Delete("/@id", "TimeblockController@destroy").name("destroy"),
    # ], prefix="/timeblocks", name="timeblocks")
]
