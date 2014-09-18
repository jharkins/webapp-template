#!/usr/bin/env python
''' 
Database Creation Script

Copied (and slightly modified) from:
http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database 

''' 
import argparse
from migrate.versioning import api
import config
import imp

from webapp.lib.db import db
import os.path

if 'APP_DEV' in os.environ:
    c = config.DevelopmentConfig
else:
    c = config.Config

parser = argparse.ArgumentParser(description='Manage WebApp database.')

parser.add_argument('action', help="action to manage the database",
choices=['create', 'migrate', 'upgrade', 'downgrade'])

def create_database():
    db.create_all()
    if not os.path.exists(c.SQLALCHEMY_MIGRATE_REPO):
        api.create(c.SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO, api.version(c.SQLALCHEMY_MIGRATE_REPO))

def migrate_database():
    migration = c.SQLALCHEMY_MIGRATE_REPO + '/versions/%03d_migration.py' % (api.db_version(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO) + 1)
    tmp_module = imp.new_module('old_model')
    old_model = api.create_model(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO)
    exec old_model in tmp_module.__dict__
    script = api.make_update_script_for_model(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO, tmp_module.meta, db.metadata)
    open(migration, "wt").write(script)
    api.upgrade(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO)
    print 'New migration saved as ' + migration
    print 'Current database version: ' + str(api.db_version(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO))

def upgrade_database():
    api.upgrade(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO)
    print 'Current database version: ' + str(api.db_version(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO))

def downgrade_database():
    v = api.db_version(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO)
    api.downgrade(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO, v - 1)
    print 'Current database version: ' + str(api.db_version(c.SQLALCHEMY_DATABASE_URI, c.SQLALCHEMY_MIGRATE_REPO))

args = parser.parse_args()

if args.action == 'create':
    create_database()
elif args.action =='migrate':
    migrate_database()
elif args.action =='upgrade':
    upgrade_database()
elif args.action =='downgrade':
    downgrade_database()
