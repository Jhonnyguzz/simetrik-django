from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import transaction_model
from .sqlalchemy_settings import mysql_engine


_file = 'transactions.csv'
_table_name = 'transactions'


@api_view(['POST'])
def load(request):
    if request.method == 'POST':
        df = pd.read_csv(_file)
        df.to_sql(_table_name, mysql_engine(), if_exists='append', index=False, chunksize=500, dtype=transaction_model)
        return HttpResponse("Success to load data from csv to database")


@api_view(['GET'])
def get_all_transactions(request):
    if request.method == 'GET':
        df = pd.read_sql_table(_table_name, mysql_engine())
        return HttpResponse(df.to_json(orient='records'), content_type="application/json")


@api_view(['GET'])
def get_transaction_by_id(request, id):
    if request.method == 'GET':
        df = pd.read_sql_table(_table_name, mysql_engine())
        return HttpResponse(df.loc[df['transaction_id'] == id].to_json(orient='records'), content_type="application/json")


@api_view(['GET'])
def search(request):
    print(request.query_params)

    query = 'SELECT * FROM {}'.format(_table_name)
    if request.query_params.get('field') and request.query_params.get('value'):
        field = request.query_params.get('field')
        value = request.query_params.get('value')
        query = query + " WHERE {} = '{}'".format(field, value)

    if request.query_params.get('orderBy'):
        orderBy = request.query_params.get('orderBy')
        query = query + " ORDER BY {}".format(orderBy)

    if request.query_params.get('skip') and request.query_params.get('limit'):
        skip = int(request.query_params.get('skip'))
        limit = int(request.query_params.get('limit'))
        query = query + " LIMIT {},{}".format(skip, limit)

    try:
        df = pd.read_sql(query, mysql_engine())
        return HttpResponse(df.to_json(orient='records'), content_type="application/json")
    except Exception:
        return HttpResponse(content="Verify query params values", status=400)
