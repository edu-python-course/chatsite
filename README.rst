###############################################################################
                            CHAT SITE DEMO PROJECT
###############################################################################

This project demonstrates the abilities of the `Django`_ framework connected
with the `Django Channels`_ extension. It is done in addition to the
`Python training course`_.

The main workflow applied in this project is described in the official tutorial
at https://channels.readthedocs.io/en/stable/tutorial/index.html.

.. _Django: https://djangoproject.com/
.. _Django Channels: https://channels.readthedocs.io/
.. _Python training course: https://github.com/shorodilov/python-course.git

Prerequisites
=============

* Python interpreter is installed

Getting started
===============

To run the project locally

#. Download the repository
#. Install all project dependencies
#. Set up environment variables
#. Run the project

It's recommended to use the virtual environment configured for the project.

The chatsite project comes with dependencies in formats suitable for `pip`_
and `poetry`_ package managers.

To install dependencies using pip do:

.. code-block::

    pip install -r requirements.txt

To do the same using poetry do:

.. code-block::

    poetry install

.. _pip: https://pip.pypa.io/
.. _poetry: https://python-poetry.org/

Before the first run ensure you got all the environment variables configured.
Refer to `Environment variables`_ section for more information.

Once all preparations are done, run the project using command:

.. code-block::

    python manage.py runserver

The output should look like:

::

    Django version 4.1.2, using settings 'chatsite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Visit the printed out URL in your web browser to see the running project.

Environment variables
=====================

This project's configuration uses some environment variables you need to set up
before running. To set the variable use command:

.. code-block::

    export VARIABLE=value  # for MacOS and Linux
    set VARIABLE=value     # for Windows

Variables table
---------------

+-----------------------+-----------------------------------------------------+
| Variable name         | Variable description                                |
+=======================+=====================================================+
| ``DJANGO_SECRET_KEY`` | The secret key is required by Django security       |
|                       | middleware. For the security reasons this can not   |
|                       | be shared across the internet, and should be setup  |
|                       | for each project individual instance separately.    |
|                       | Here is a good service to get it:                   |
|                       | https://djecrety.ir/                                |
+-----------------------+-----------------------------------------------------+

Run with Docker Compose
=======================

Create ``.env`` file to run application in a container. Use ``.env.sample``
as a reference.

.. code-block::

    docker-compose up --build
