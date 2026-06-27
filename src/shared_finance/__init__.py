from flask import Flask

from shared_finance.api.health import health_bp
from shared_finance.api.expenses import expenses_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(health_bp)
    app.register_blueprint(expenses_bp)

    return app