from .application import create_app
from .settings import Config


app = create_app(Config)