# Flask Application Starting Template

This is a Flask application template with all the trimmings. You can use it to
start a web application and have access to all of these awesome technologies:

1. Flask (and associated goodies)
2. Flask-Login to manage session login and logout.
3. Flask-SQLAlchemy for database management.
4. SQLAlchemy-migrate to keep track of database updates.
5. Twitter Bootstrap for HTML/CSS stuff.
6. jQuery and loDash for JS stuff.

## Quick Start

1. Download (or fork, or whatever) the repository.
2. Create a virtual environment `virtualenv venv`
3. Activate the venv `source venv/bin/activate`
4. Get the requirements `pip install -r requirements.txt`
5. Change the config.py stuff to suit your needs.
6. Change the secret key in `webapp/__init__.py` to something different (this is
   for security purposes).
7. If you would just like to try this out without much customizing, you can use

    ./db_manage.py create

   The above will create a sqlite3 database with the User schema cooked in.

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
13. sqlalchemy-migrate==0.9.2

## Database Migration

Database management (create, migrate, upgrade, downgrade) uses scripts created by Miguel
Grinberg. All credit is to his Flask Mega Tutorial blog posts. The database
stuff can be seen here:
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database

All of the management scripts from the blog post from Miguel have been added to
a single file, db_manage.py. It has create, migrate, upgrade and downgrade
options included.

## Development

This app uses a bash environment variable to control if it's in development
mode. In order to use dev mode: `export APP_DEV=1`
