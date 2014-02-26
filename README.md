# Flask Application Starting Template

This is a Flask application template with all the trimmings. You can use it to
start a web application and have access to all of these awesome technologies:

1. Flask (and associated goodies)
2. Flask-Login to manage session login and logout.
3. Flask-SQLAlchemy for database management
3. Twitter Bootstrap for HTML/CSS stuff.
4. jQuery and loDash for JS stuff.

## Notes

Authentication and registration is hooked in with Flask-SQLAlchemy and
Flask-Login. The system uses a sqlite3 database by default, but that's easy to
change by updating the config.py file. Passwords are stored in the sqlite3
database using `werkzeug.security.generate_password_hash` - it is suggested that
you review this behavior to ensure this is what you really want.

## Requirements

The following are the python requirements for the project. Everything here is 
included in a requirements.txt file that can be used with pip.

1. Flask==0.10.1
2. Flask-Login==0.2.9
3. Flask-SQLAlchemy==1.0
4. Flask-WTF==0.9.4
5. Jinja2==2.7.2
6. MarkupSafe==0.18
7. SQLAlchemy==0.9.3
8. WTForms==1.0.5
9. Werkzeug==0.9.4
10. itsdangerous==0.23
11. python-ldap==2.4.14
12. wsgiref==0.1.2

## Development

This app uses a bash environment variable to control if it's in development
mode. In order to use dev mode: `export APP_DEV=1`
