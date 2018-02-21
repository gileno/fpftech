from .application import create_app
from .settings import ProductionConfig


app = create_app(ProductionConfig)
