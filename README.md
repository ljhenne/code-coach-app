# Code Coach

Django-based app.

# Useful commands

Start the database

```shell
pg_ctl -D code-coach-local -l logfile start
```

Run migrations on local database

```shell
python manage.py migrate --settings code_coach.settings_local
```

# Next steps

- Go through the [Django Quickstart](https://manage.auth0.com/dashboard/us/loganjhennessy/applications/P4jLYuCVKAkhmIroCzlevKpNBsrIjQLS/quickstart)
- Go through the [Django Authentication Tutorial](https://auth0.com/blog/django-authentication/)
- Use that knowledge to put authentication in my app.
- Add the User model to the problem model.
- This should be enough to get a single problem attempt to show up on the UI.
- Add a simple landing page as a separate Django app.