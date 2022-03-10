from src import app_view

from src.controller.view.home import HomeController

app_view.add_resource(HomeController, '/')
