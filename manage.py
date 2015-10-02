#!/usr/bin/env python
import os
import sys
#sys.path.append('/C/Users/grael_000/.virtualenvs/bookstore-django/Scripts/python')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
