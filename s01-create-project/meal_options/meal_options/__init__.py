from .app_factory import create_app

app = create_app('meal_options.settings.DevConfig')

from . import views

