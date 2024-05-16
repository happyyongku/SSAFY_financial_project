from django.shortcuts import render, get_object_or_404
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import (
    FinancialCompany, 
    DepositOption, 
    DepositProduct, 
    InstallmentSavingOption,
    InstallmentSavingProduct,
    PensionOption,
    PensionProduct
    )
from .serializers import (
    FinancialCompanySerializer,
    DepositOptionSerializer,
    DepositProductSerializer,
    InstallmentSavingOptionSerializer,
    InstallmentSavingProductSerializer,
    PensionOptionSerializer,
    PensionProductSerializer
)

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
        response = requests.get(url, params=params_request[idx]).json()['result']
        # ---test ---
        if idx == 1:
            test_data = response
        #-------------------------
        if idx == 1:
            for product in response['baseList']:
                fin_cd = product['fin_co_no']
                if not FinancialCompany.objects.filter(fin_co_no=fin_cd).exists():
                    company = {
                        'kor_co_nm': product['kor_co_nm'],
                        'fin_co_no': product['fin_co_no']
                    }
                    company_serializer = FinancialCompanySerializer(data=company)
                    if company_serializer.is_valid(raise_exception=True):
                        company_serializer.save()
                frgn_cmp_dps_prdt = FinancialCompany.objects.get(fin_co_nm=product['fin_co_no'])
                d_product_data = {
                    'fin_co_no': frgn_cmp_dps_prdt,
                    'fin_prdt_cd': product['fin_prdt_cd'],
                    'fin_prdt_nm': product['fin_prdt_nm'],
                    'mtrt_int': product['mtrt_int'],
                    'spcl_cnd': product['spcl_cnd'],
                    'join_member': product['join_member'],
                    'max_limit': product['max_limit'],
                    'etc_note': product['etc_note']
                }
                d_prdt_serializer = DepositProductSerializer(data=d_product_data)
                if d_prdt_serializer.is_valid(raise_exception=True):
                    d_prdt_serializer.save()
            for option in response['optionList']:
                frgn_cmp_dps_opt = FinancialCompany.objects.get(fin_co_no=option['fin_co_no'])
                frgn_prdt_dps_opt = DepositProduct.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
                d_option_data = {
                    'fin_prdt_cd': frgn_prdt_dps_opt,
                    'fin_co_no': frgn_cmp_dps_opt,
                    'intr_rate_type': option['intr_rate_type'],
                    'intr_rate_type_nm': option['intr_rate_type_nm'],
                    'save_trm': int(option['save_trm']),
                    'intr_rate': option['intr_rate'],
                    'intr_rate2': option['intr_rate2']
                    
                }
                d_option_serializer = DepositOptionSerializer(data=d_option_data)
                if d_option_serializer.is_valid(raise_exception=True):
                    d_option_serializer.save()
                    
                
    
    return Response(test_data, status=status.HTTP_200_OK)
        