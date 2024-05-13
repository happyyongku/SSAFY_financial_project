from django.shortcuts import render, get_object_or_404
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def get_data(request):
    api_key = settings.API_KEY_FINANCIAL
    product_request = ['depositProductsSearch', 'savingProductsSearch', 'annuitySavingProductsSearch']
    params_request = [
        {
            'auth':api_key,
            'topFinGrpNo':'020000',
            'pageNo':1,
        },
        {
            'auth':api_key,
            'topFinGrpNo':'020000',
            'pageNo':1,
        },
        {
            'auth':api_key,
            'topFinGrpNo':'060000',
            'pageNo':1
        }
    ]
    for idx in range(len(product_request)):
        url = f'http://finlife.fss.or.kr/finlifeapi/{product_request[idx]}.json'
        response = requests.get(url, params=params_request[idx]).json()
        if idx == 1:
            print(response)
    
    return Response(status=status.HTTP_200_OK)
        