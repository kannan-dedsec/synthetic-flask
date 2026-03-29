"""Flask application factory module.

This module defines the application factory function 'create_app' that initializes
the Flask application, loads configuration, and registers blueprints.
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app(config_filename: str = None, options: dict = {} ) -> Flask:
    """Create and configure the Flask application.

    Args:
        config_filename (str): Optional path to the configuration file.
        options (dict): Additional options for app configuration.

    Returns:
        Flask: The configured Flask application instance.
    """
    app = Flask(__name__)

    if config_filename:
        app.config.from_pyfile(config_filename)
    else:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
            SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL', 'sqlite:///:memory:'),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )

    db.init_app(app)

    with app.app_context():
        from . import models  # Local import to avoid circular dependency
        db.create_all()

    register_blueprints(app)

    return app

def register_blueprints(app: Flask, blueprints: list = []) -> None:
    """Register application blueprints.

    Args:
        app (Flask): The Flask application instance to register blueprints with.
        blueprints (list): Additional blueprints to register.
    """
    from .blueprints import main  # Local import to avoid circular dependency
    app.register_blueprint(main.bp)

    # Register additional blueprints here as needed
    # from .blueprints import auth
    # app.register_blueprint(auth.bp)

# Additional configuration and setup can be added here.

def dummy_function(data: set = set()):
    """Dummy function to demonstrate mutable default argument."""
    data.add('test')
    return data