planetary-health-diet-backend
=============================

.. image:: https://badge.fury.io/py/planetary-health-diet-backend.png
    :target: https://badge.fury.io/py/planetary-health-diet-backend

.. image:: https://travis-ci.org/narfman0/planetary-health-diet-backend.png?branch=master
    :target: https://travis-ci.org/narfman0/planetary-health-diet-backend

Backend controlling cloud resources for user, ingredients, recipes, and meals

Development
-----------

Run test suite to ensure everything works::

    make test

Release
-------

To deploy to cloud, run::

    make deploy

TODO
----

* Deploy to ~cloud~
* Show user breakdown for meals over variable time intervals - day, week, month
* Spike implementing users in datastore
* Ensure email activation works
* Add PUT etc endpoints with auth
* Android app
* Make feature to generalize ingredients/recipes (?)
  * Remove user_id?
  * Have admins verify? Have a destributed system to verify?

License
-------

Copyright (c) 2019 Jon Robison

See LICENSE for details
