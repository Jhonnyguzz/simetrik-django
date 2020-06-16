"""""""""""""""""
Transactions
"""""""""""""""""

Manages transactions, those are loaded from csv local file using pandas and then are saved to AWS RDS, the purpose is
implementing a REST API to get access to the data from database

.. contents:: Overview
   :depth: 3

===================
How to run
===================

This project was built using python 3.7

All python modules needed are specified in requirements.txt file, install them in the python environment
that you're going to use to run this application. For standard environment:

.. sourcecode::

  pip install -r requirements.txt

Then proceed to run the dev environment into project folder

.. sourcecode::

  python manage.py runserver


===================
How to use
===================

----------------------
REST API
----------------------

- POST localhost:8000/v1/load

    Upload the csv file to SQL database in AWS with the default file transactions.csv

- GET localhost:8000/v1/getAll

    It returns all transactions saved in database in JSON format

- GET localhost:8000/v1/get/:id

    It returns the specified transaction(s) with the given transaction_id

- GET localhost:8000/v1/search

    It returns the transaction(s) using filtering, pagination and order according to query parameters provided

    * skip and limit: integer values to paginate
    * orderBy: string with field name to order
    * field and value: field and value to filter

    example: localhost:8000/v1/search?field=transaction_amount&value=15000&skip=1&limit=5&orderBy=client_id

    * **NOTE**: the same invocation as getAll if no query parameters are given