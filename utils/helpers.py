"""Utility functions for a Flask project.

This module provides various helper functions including:
- Formatting datetime objects.
- Slugifying strings for URL-friendly usage.
- Paginating query results.
- Sending emails using Flask-Mail.
"""

from datetime import datetime
from typing import List, Any, Dict
from urllib.parse import quote_plus
from flask import request
from flask_mail import Mail, Message


def format_datetime(dt: datetime, format_string: str = '%Y-%m-%d %H:%M:%S') -> str:
    """Format a datetime object into a string.

    Args:
        dt (datetime): The datetime object to format.
        format_string (str): The format string.

    Returns:
        str: The formatted datetime string.
    """
    return dt.strftime(format_string)


def slugify(text: str) -> str:
    """Convert a string to a URL-friendly slug.

    Args:
        text (str): The input string to slugify.

    Returns:
        str: The slugified string.
    """
    return quote_plus(text.lower().replace(' ', '-').replace('_', '-'))


def paginate_query(query: Any, page: int, per_page: int) -> Dict[str, Any]:
    """Paginate a database query result.

    Args:
        query (Any): The SQLAlchemy query object to paginate.
        page (int): The page number to retrieve.
        per_page (int): The number of items per page.

    Returns:
        Dict[str, Any]: A dictionary containing the paginated results and metadata.
    """
    total_items = query.count()
    items = query.offset((page - 1) * per_page).limit(per_page).all()
    return {
        'items': items,
        'total': total_items,
        'page': page,
        'per_page': per_page,
        'pages': (total_items + per_page - 1) // per_page
    }


def send_email(subject: str, recipients: List[str], body: str) -> None:
    """Send an email using Flask-Mail.

    Args:
        subject (str): The subject of the email.
        recipients (List[str]): The list of recipient email addresses.
        body (str): The body of the email.

    Raises:
        Exception: If the email fails to send.
    """
    mail = Mail()
    msg = Message(subject, recipients=recipients)
    msg.body = body
    try:
        mail.send(msg)
    except Exception as e:
        raise Exception(f"Failed to send email: {e}") from e