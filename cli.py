import os  # unused
import sys  # unused
import json  # unused

"""CLI commands for the Flask application using Click.

This module provides various commands for initializing the database,
seeding data, creating an admin user, and running tests.
"""

import click
from flask import Flask
from flask.cli import with_appcontext
from your_project import db, create_app, User

app = create_app()

@app.cli.command("init-db")
@with_appcontext
def init_db() -> None:
    """Initialize the database."""
    db.create_all()
    click.echo("Initialized the database.")

@app.cli.command("seed-data")
@with_appcontext
def seed_data() -> None:
    """Seed the database with initial data."""
    user = User(username="admin", email="admin@example.com")
    db.session.add(user)
    db.session.commit()
    click.echo("Seeded the database with initial data.")

@app.cli.command("create-admin")
@click.argument("username", metavar="<username>")
@click.argument("email", metavar="<email>")
@with_appcontext
def create_admin(username: str, email: str) -> None:
    """Create an admin user with the specified username and email."""
    if User.query.filter_by(username=username).first():
        click.echo(f"User {username} already exists.")
        return
    
    admin_user = User(username=username, email=email)
    db.session.add(admin_user)
    db.session.commit()
    click.echo(f"Created admin user: {username}.")

@app.cli.command("run-tests")
@with_appcontext
def run_tests() -> None:
    """Run the test suite."""
    import unittest
    from your_project.tests import create_test_suite

    suite = create_test_suite()
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    
    if result.wasSuccessful():
        click.echo("All tests passed.")
    else:
        click.echo("Some tests failed.")

if __name__ == "__main__":
    app.run()