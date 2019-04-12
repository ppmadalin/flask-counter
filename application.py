from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# setup db
db = SQLAlchemy()


def create_app(**config):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # Apply updated configs
    app.config.update(config)

    # Initialize database
    db.init_app(app)
    migrate = Migrate(app, db)

    # Import blueprints
    from counter.views import counter_app

    # Register blueprints
    app.register_blueprint(counter_app)

    return app
