Djankan
=======

Djankan is a flexible kanban solution made with meteor plugging into a Django API.

Features
--------

    - Drag-and-drop task 'cards'
    - realtime updating
    - custom lanes (priorities)
    - multiple boards
    - group cards with buckets
    - robust API

Requirements
------------

    1. postgreSQL
    2. django
    3. REST-Framework (http://www.django-rest-framework.org/#installation)


Installation
------------

    1. create a postgreSQL database called djankan
       - sudo su - postgres
       - createuser -P <<yourdesiredusername>>
       - createdb djankan
    2. grant all privalages on djankan to a user
       - psql
       - GRANT ALL PRIVILIGES ON DATABASE djankan to <<yourdesiredusername>>;
    4. logout of postgreSQL
       - $ logout
    3. change djankan/djankan/settings.py lines 66 - 73 to be
        DATABASES = {
            'default': {
               'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'djankan',
                'USER': '<<yourdesiredusername>>',
                'PASSWORD': '<<yourdesiredpassword>>',
            }
        }
    4. do
       - $ python manage.py syncdb
    5. finally run the server
       - $ python manage.py runserver

Contribute
----------

- Source Code: https://github.com/CodethinkLabs/Djankan

License
-------

The MIT License (MIT)

Copyright (c) 2014 Codethink Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
