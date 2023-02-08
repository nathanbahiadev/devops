from decouple import config

from src.configs.settings.development import DevelopmentConfig
from src.configs.settings.production import ProductionConfig


environment = {
    'DEVELOPMENT': DevelopmentConfig,
    'PRODUCTION': ProductionConfig
 }[config("ENV", default="DEVELOPMENT")]

