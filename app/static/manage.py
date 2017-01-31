# #!/usr/bin/env python
# import os
# import sys

# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

#     from django.core.management import execute_from_command_line

#     execute_from_command_line(sys.argv)

# manage.py

from flask import Manager

from app import app

manager = Manager(app)

@manager.command
def hello():
    print "hello"

if __name__ == "__main__":
    manager.run()