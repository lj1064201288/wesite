#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    profile = os.environ.get('TYPEIDEA_PROFILE', 'develop')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "typeidea.settings.%s" % profile)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
