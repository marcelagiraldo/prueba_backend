from flask import Flask
from os import environ
def create_app():
 app = Flask(__name__,
 instance_relative_config=True)

 app.config['ENVIRONMENT'] = environ.get("ENVIRONMENT")
 config_class = 'config.DevelopmentConfig'

 match app.config['ENVIRONMENT']:
 case "development":
 config_class = 'config.DevelopmentConfig'
 case "production":
 config_class = 'config.ProductionConfig'
 case _:
 print(f"ERROR: environment unknown: {app.config.get('ENVIRONMENT')},
fallback to {mode}")
 app.config['ENVIRONMENT'] = "development"
 app.config.from_object(config_class)

 return app
