"""
Helper functions for BrightSmile Dental Clinic
CS50-style helper functions
"""

from functools import wraps
from flask import session, redirect, url_for, flash, render_template


def login_required(f):
    """
    Decorate routes to require login.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


def apology(message, code=400):
    """
    Render message as an apology to user.
    """
    def escape(s):
        """
        Escape special characters.
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message))

