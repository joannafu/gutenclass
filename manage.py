#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    
    ENV = os.environ['MY_PROJECT_ENV']
    if ENV == 'production':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseclass.settings.prod")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courseclass.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
