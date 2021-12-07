"""Web Routes."""

from masonite.routes import Get, Post, Put, Delete, RouteGroup

ROUTES = [
    Get("/", "WelcomeController@show").name("welcome"),
    RouteGroup([
        Get("/", "TimeblockController@index").name("index"),
        Get("/@id", "TimeblockController@show").name("show"),
        Post("/", "TimeblockController@create").name("create"),
        Put("/@id", "TimeblockController@update").name("update"),
        Delete("/@id", "TimeblockController@destroy").name("destroy"),
    ], prefix = "/timeblocks", name = "timeblocks")
]
