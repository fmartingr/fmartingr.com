# -*- coding: utf-8 -*-

"""
Script to perform the migration from the old blog database
to the lektor file format.
"""

import os.path

import dataset


SQLITE = os.path.expanduser('~/NextCloud/Backups/blog/v2/database.sqlite')
LEKTOR = os.path.expanduser('~/Developer/fmartingr-lektor/content')

db = dataset.connect('sqlite:///' + SQLITE)

posts = db['blog_entry']
projects = db['projects_project']
project_images = lambda x: db['projects_projectimage'].filter(project_id=x)
get_project_group = lambda x: db['projects_group'].filter(id=x)
