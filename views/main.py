"""Main routes for the Flask application.

This module defines the main routes including index, about, and dashboard.
The dashboard route is protected by a login_required decorator.
"""

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index() -> str:
    """Render the index page.

    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template("index.html")

@main_bp.route("/about")
def about() -> str:
    """Render the about page.

    Returns:
        str: Rendered HTML of the about page.
    """
    return render_template("about.html")

@main_bp.route("/dashboard")
@login_required
def dashboard() -> str:
    """Render the dashboard page, requires user to be logged in.

    Returns:
        str: Rendered HTML of the dashboard page.
    """
    return render_template("dashboard.html")