release: python runna/manage.py setup_project && python runna/manage.py populate_database
web: gunicorn runna.wsgi:application
