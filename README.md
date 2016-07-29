# Sihoo

*V 0.0.1*

## What's Sihoo

## Requirements

+ Python 3.4+
+ [Tornado](http://www.tornadoweb.org/en/stable/)
+ Flask
+ PostgreSQL
+ Celery
+ Redis
+ Bootstrap

Python 2 is **not** supported.

All the python version prior to 3.4 are not tested, they may work fine, or not (more likely). 

Sihoo uses Tornado to handle tens of thousands live connection from browser, but only for this part.

Regular web requests are handled by Flask.

PostgresSQL and Redis is the database backend, they persistent, cache and backup all the data.

## Testing

Sihoo uses [nosetest](http://nose.readthedocs.io/en/latest/index.html)

To run all test, just do:

    nosetests

*Notice:*

1. nosetest will lookup all the source files and do test with those looks like a test.
2. By default, nosetest will skip all the files that are executable, this maybe annoying in some circumstances, if you find your test case number 
is 0, try turn off the option by:

        nosetests --exe

**make sure it's safe before you do this.**


## Deployment

Sihoo is under construction currently, if you wanna check out the lastest progress, you can run it with:

    python manage.py start

Need help? please check:

    python manage.py --help
