"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
        Get("/", "TimeblockController@indexTimeblock").name("indexTimeblock"),
        Get("/@id", "TimeblockController@showTimeblock").name("showTimeblock"),
        Post("/", "TimeblockController@createTimeblock").name("createTimeblock"),
        Put("/@id", "TimeblockController@updateTimeblock").name("updateTimeblock"),
        # Delete("/@id", "TimeblockController@destroyTimeblock").name("destroyTimeblock"),
    ], prefix = "/timeblocks", name = "timeblocks"),

    RouteGroup([
        Get("/", "TimeblockController@indexReminder").name("indexReminder"),
        Get("/@id", "TimeblockController@showReminder").name("showReminder"),
        Post("/", "TimeblockController@createReminder").name("createReminder"),
        Put("/@id", "TimeblockController@updateReminder").name("updateReminder"),
        Delete("/@id", "TimeblockController@destroyReminder").name("destroyReminder"),
    ], prefix = "/reminders", name = "reminders"),
]
