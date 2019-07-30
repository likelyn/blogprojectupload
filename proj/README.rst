=====
loginapp
=====

loginapp is a simple Django app to conduct Web-based loginapp. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "loginapp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'loginapp',
    ]

2. Include the loginapp URLconf in your project urls.py like this::

    path('loginapp/', include('loginapp.urls')),

3. Run `python manage.py migrate` to create the loginapp models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/loginapp/ to participate in the poll.