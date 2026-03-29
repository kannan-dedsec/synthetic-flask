"""Forms module for handling post and comment submissions using WTForms.

This module defines the PostForm and CommentForm classes, which are used
to validate user input for creating posts and comments in a Flask application.
"""

from typing import Any
from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    """Form for creating a new post."""

    title: StringField = StringField(
        'Title',
        validators=[
            DataRequired(message='Title is required.'),
            Length(min=5, max=100, message='Title must be between 5 and 100 characters.')
        ]
    )
    
    content: TextAreaField = TextAreaField(
        'Content',
        validators=[
            DataRequired(message='Content is required.'),
            Length(min=40, max=1500, message='Content must be between 40 and 1500 characters.')
        ]
    )

    def validate(self) -> bool:
        """Override the default validate method to add custom validation if needed."""
        return super().validate()


class CommentForm(FlaskForm):
    """Form for adding a comment to a post."""

    content: TextAreaField = TextAreaField(
        'Comment',
        validators=[
            DataRequired(message='Comment is required.'),
            Length(min=1, max=500, message='Comment must be between 1 and 500 characters.')
        ]
    )

    def validate(self) -> bool:
        """Override the default validate method to add custom validation if needed."""
        return super().validate()