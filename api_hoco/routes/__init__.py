from .api import api_blueprints

def init_app(app):
    app.register_blueprint(api_blueprints)

