from .api import api_blueprints
from .orgs import orgs_blueprints
from .questions import questions_blueprints


def init_app(app):
    app.register_blueprint(api_blueprints)
    app.register_blueprint(orgs_blueprints)
    app.register_blueprint(questions_blueprints)

