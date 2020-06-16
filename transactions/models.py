from django.db import models

# Create your models here.

from sqlalchemy.types import Date, VARCHAR, Numeric

transaction_model = {
            'transaction_id': VARCHAR(255),
            'transaction_date': Date,
            'transaction_amount': Numeric,
            'client_id': Numeric,
            'client_name': VARCHAR(255)
        }
