release: python runna/manage.py setup_project && python runna/manage.py populate_database && python runna/manage.py collectstatic
web: gunicorn runna.wsgi:application
