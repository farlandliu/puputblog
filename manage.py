#!/usr/bin/env python
import os
import sys
import dotenv
if __name__ == '__main__':
    dotenv.read_dotenv()
    configuration = os.getenv('ENVIRONMENT', 'development').title()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', configuration)

    try:
        from configurations.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Couldn\'t import Django. Are you sure it\'s installed and '
            'available on your PYTHONPATH environment variable? Did you '
            'forget to activate a virtual environment?') from exc
    execute_from_command_line(sys.argv)
