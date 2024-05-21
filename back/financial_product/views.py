from django.shortcuts import render, get_object_or_404
import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import pandas as pd
from openai import OpenAI
from datetime import date, datetime, timedelta
import pymysql
import json
from .models import (
    FinancialCompany, 
    DepositOption, 
    DepositProduct, 
    InstallmentSavingOption,
    InstallmentSavingProduct,
    ExchangRate
    )
from .serializers import (
    FinancialCompanySerializer,
    DepositOptionSerializer,
    DepositProductSerializer,
    InstallmentSavingOptionSerializer,
    InstallmentSavingProductSerializer,
    ExchangeRateSerializer
)

chat_history = []

# Create your views here.

@api_view(['POST'])
def get_financial_data(request):
    api_key = settings.API_KEY_FINANCIAL
    product_request = ['depositProductsSearch', 'savingProductsSearch']
    params_request = [
        {
            'auth':api_key,
            'topFinGrpNo':'020000',
            'pageNo':2,
        },
        {
            'auth':api_key,
            'topFinGrpNo':'020000',
            'pageNo':1,
        },
    ]
    for idx in range(len(product_request)):
        url = f'http://finlife.fss.or.kr/finlifeapi/{product_request[idx]}.json'
        
        # --------------------- 정기 예금 -----------------------------------------
        if idx == 0:
            for GrpNo in ['020000', '030300']:
                params_request[idx]['topFinGrpNo'] = GrpNo
                page = 1
                while True:
                    params_request[idx]['pageNo'] = page
                    page += 1
                    response = requests.get(url, params=params_request[idx]).json()['result']
                    if response['max_page_no'] < response['now_page_no']:
                        break
                    for product in response['baseList']:
                        fin_cd = product['fin_co_no']
                        company_data = {
                            'kor_co_nm': product['kor_co_nm'],
                            'fin_co_no': product['fin_co_no']
                        }
                        
                        company, created = FinancialCompany.objects.update_or_create(
                            fin_co_no=fin_cd,
                            defaults=company_data
                        )
                        
                        d_product_data = {
                            'fin_co_no': company,  # ForeignKey relationship
                            'kor_co_nm': product['kor_co_nm'],
                            'fin_prdt_cd': product['fin_prdt_cd'],
                            'fin_prdt_nm': product['fin_prdt_nm'],
                            'mtrt_int': product['mtrt_int'],
                            'spcl_cnd': product['spcl_cnd'],
                            'join_member': product['join_member'],
                            'max_limit': product['max_limit'],
                            'etc_note': product['etc_note']
                        }
                        
                        DepositProduct.objects.update_or_create(
                            fin_co_no=company,
                            fin_prdt_cd=product['fin_prdt_cd'],
                            defaults=d_product_data
                        )
                    for option in response['optionList']:
                        company_dps_opt = FinancialCompany.objects.get(fin_co_no=option['fin_co_no'])
                        product_dps_opt = DepositProduct.objects.get(
                            fin_prdt_cd=option['fin_prdt_cd'], 
                            fin_co_no=company_dps_opt
                            )
                        
                        d_option_data = {
                            'fin_prdt_cd': product_dps_opt,
                            'fin_co_no': company_dps_opt,
                            'intr_rate_type': option['intr_rate_type'],
                            'intr_rate_type_nm': option['intr_rate_type_nm'],
                            'save_trm': int(option['save_trm']),
                            'intr_rate': option['intr_rate'],
                            'intr_rate2': option['intr_rate2'],
                            'dcls_month': option['dcls_month']
                        }
                        try:
                            DepositOption.objects.update_or_create(
                                fin_prdt_cd = product_dps_opt,
                                dcls_month=company_dps_opt,
                                defaults=d_option_data
                            )
                        except:
                            continue
                        
        # ---------------------------- 적금 -------------------------------------
        if idx == 1:
            for GrpNo in ['020000', '030300']:
                params_request[idx]['topFinGrpNo'] = GrpNo
                page = 1
                while True:
                    params_request[idx]['pageNo'] = page
                    page += 1
                    response = requests.get(url, params=params_request[idx]).json()['result']
                    if response['max_page_no'] < response['now_page_no']:
                        break
                    test_data = response
                    for product in response['baseList']:
                        fin_cd = product['fin_co_no']
                        company_data = {
                            'kor_co_nm': product['kor_co_nm'],
                            'fin_co_no': product['fin_co_no']
                        }
                        
                        company, created = FinancialCompany.objects.update_or_create(
                            fin_co_no=fin_cd,
                            defaults=company_data
                        )
                        
                        i_product_data = {
                            'fin_co_no': company,  # ForeignKey relationship
                            'kor_co_nm': product['kor_co_nm'],
                            'fin_prdt_cd': product['fin_prdt_cd'],
                            'fin_prdt_nm': product['fin_prdt_nm'],
                            'mtrt_int': product['mtrt_int'],
                            'spcl_cnd': product['spcl_cnd'],
                            'join_member': product['join_member'],
                            'max_limit': product['max_limit'],
                            'etc_note': product['etc_note']
                        }
                        try:
                            InstallmentSavingProduct.objects.update_or_create(
                                fin_co_no=company,
                                fin_prdt_cd=product['fin_prdt_cd'],
                                defaults=i_product_data
                            )
                        except:
                            continue
                        
                    for option in response['optionList']:
                        company_ins_opt = FinancialCompany.objects.get(fin_co_no=option['fin_co_no'])
                        product_ins_opt = InstallmentSavingProduct.objects.get(
                            fin_prdt_cd=option['fin_prdt_cd'], 
                            fin_co_no=company_ins_opt
                            )
                        
                        i_option_data = {
                            'fin_prdt_cd': product_ins_opt,
                            'fin_co_no': company_ins_opt,
                            'intr_rate_type': option['intr_rate_type'],
                            'intr_rate_type_nm': option['intr_rate_type_nm'],
                            'save_trm': int(option['save_trm']),
                            'intr_rate': option['intr_rate'],
                            'intr_rate2': option['intr_rate2'],
                            'rsrv_type': option['rsrv_type'],
                            'rsrv_type_nm': option['rsrv_type_nm'],
                            'dcls_month': option['dcls_month'],
                        }
                        try:
                            InstallmentSavingOption.objects.update_or_create(
                                fin_prdt_cd = product_ins_opt,
                                dcls_month=company_ins_opt,
                                defaults=i_option_data
                            )
                        except:
                            continue
        
        
    
    return Response(test_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def check_data(request):
    deposit_p = DepositProduct.objects.all()
    deposit_o = DepositOption.objects.all()
    install_p = InstallmentSavingProduct.objects.all()
    install_o = InstallmentSavingProduct.objects.all()

    
    df_d_p = pd.DataFrame(list(deposit_p.values()))
    df_d_o = pd.DataFrame(list(deposit_o.values()))
    df_i_p = pd.DataFrame(list(install_p.values()))
    df_i_o = pd.DataFrame(list(install_o.values()))
    dupldict = {
        'd_p' : df_d_p.duplicated().sum(),
        'd_o' : df_d_o.duplicated().sum(),
        'i_p' : df_i_p.duplicated().sum(),
        'i_o' : df_i_o.duplicated().sum(),

    }
    return Response(dupldict)
    
@api_view(['POST'])
def get_exchange_data(request):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    api_key = settings.API_KEY_EXCHANGE
    params = {
        'authkey': api_key,
        'data': 'AP01',

    }
    today = date.today()
    response = requests.get(url, params=params).json()
    if not response:
        return
    
    for rate in response:
        if rate['cur_unit'] == 'KRW':
                continue
        ttb_str = rate['ttb'].replace(',','')
        tts_str = rate['tts'].replace(',','')
        deal_str = rate['deal_bas_r'].replace(',','')
        rate_data = {
            'date':today,
            'cur_unit': rate['cur_unit'],
            'cur_nm': rate['cur_nm'],
            'ttb': float(ttb_str),
            'tts': float(tts_str),
            'deal_bas_r': float(deal_str)
        }
        ExchangRate.objects.update_or_create(
                                cur_unit=rate['cur_unit'],
                                date = today,
                                defaults=rate_data
                            )
    
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def get_exchange_term_data(request, start_date):
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    api_key = settings.API_KEY_EXCHANGE
    params = {
        'authkey': api_key,
        'searchdate': None,
        'data': 'AP01'
    }
    now = datetime.now()
    
    start = datetime.strptime(start_date, "%Y-%m-%d")
    date_list = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((now - start).days + 1)]
    
    for cur_date in date_list:
        params['searchdate'] = cur_date
        response = requests.get(url, params=params).json()
        print(response)
        if not response:
            continue
        for rate in response:
            if rate['cur_unit'] == 'KRW':
                continue
            ttb_str = rate['ttb'].replace(',','')
            tts_str = rate['tts'].replace(',','')
            deal_str = rate['deal_bas_r'].replace(',','')
            rate_data = {
                'date':cur_date,
                'cur_unit': rate['cur_unit'],
                'cur_nm': rate['cur_nm'],
                'ttb': float(ttb_str),
                'tts': float(tts_str),
                'deal_bas_r': float(deal_str)
            }
            ExchangRate.objects.update_or_create(
                                    cur_unit=rate['cur_unit'],
                                    date = cur_date,
                                    defaults=rate_data
                                )
    
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_rate(request, date):
    rate = ExchangRate.objects.filter(date=date)
    serializer = ExchangeRateSerializer(rate, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
            
@api_view(['GET'])
def get_bank_list(request):
    banks = FinancialCompany.objects.all()
    serializer = FinancialCompanySerializer(banks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product_list(request, type, bank_id):
    bank = FinancialCompany.objects.get(pk=bank_id)
    if type == 'deposit':
        products = bank.depositproduct_set.all()
        serializer = DepositProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif type == 'installment':
        products = bank.installmentsavingproduct_set.all()
        serializer = InstallmentSavingProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_option_list(request, type, product_id):
    print('////////////////////////////////////////////')
    if type == 'deposit':
        product = DepositProduct.objects.get(pk=product_id)
        options = product.depositoption_set.all()
        serializer = DepositOptionSerializer(options, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif type == 'installment':
        product = InstallmentSavingProduct.objects.get(pk=product_id)
        options = product.installmentsavingoption_set.all()
        serializer = InstallmentSavingOptionSerializer(options, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def fetch_product(request, type):
    print('/////////////////')
    if type=='deposit':
        deposits = DepositProduct.objects.all()
        serializer = DepositProductSerializer(deposits, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif type=='installment':
        installment = InstallmentSavingProduct.objects.all()
        serializer = InstallmentSavingProductSerializer(installment, many=True)
        return Response(serializer, status=status.HTTP_200_OK)


# DB 내의 상품과 옵션 데이터를 fixture (json이나 csv)로 만들고 아래 코드로 읽어서 bank_info에 넣기
company_info = []
deposit_info = []
installment_info = []
# with open('파일경로', 'r', encoding='utf-8') as f :
#     text = f.read()
conn = pymysql.connect(
    host='localhost',
    user='yonggu97',
    password = settings.DB_PASSWORD,
    db = 'ssafy_final'
)
cursor = conn.cursor()
db_list = [
    'financial_product_financialcompany',
    # 'financial_product_depositoption',
    'financial_product_depositproduct',
    # 'financial_product_installmentsavingoption',
    'financial_product_installmentsavingproduct'
    ]

for db in db_list:
    if 'company' in db:
        cursor.execute(f"SELECT * FROM {db}")
    else :
        cursor.execute(f'SELECT kor_co_nm,  mtrt_int FROM {db}')
        
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    json_data = df.to_json(orient='records', force_ascii=False)
    if 'company' in db:
        company_info.extend(json.loads(json_data))
    elif 'deposit' in db:
        deposit_info.extend(json.loads(json_data))
    elif 'installment' in db:
        installment_info.extend(json.loads(json_data))

conn.close()


@api_view(['GET'])
def chatAI(request):
    global chat_history
    print('//////')
    API_KEY = settings.API_KEY_AI
    client = OpenAI(api_key=API_KEY)
    input_message = request.query_params.get('message','')
    print(input_message)
    #아래 정보에 기반해서 답변해줘야해 {bank_info}
    chat_history.extend(
        [
            {"role": "user", "content": f"{input_message}"},
            {"role": "system", "content": f"반드시 한글로 대답해줘."}
        ] 
    )
    
    if '은행' in input_message and '추천' in input_message:
        print(company_info[0])
        chat_history.append(
            {"role": "system", "content": f"만약 은행을 추천한다면 아래 정보에 기반해서 한글로 답변해줘. {company_info}"}
        )
    if '예금' in input_message and '추천' in input_message:
        chat_history.append(
            {"role": "system", "content": f"만약 예금 상품을 추천한다면 아래 정보에 기반해서 예금 상품의 이름과 함께 정보를 한글로 답변해줘. {deposit_info} 예금 상품의 이름은 각 딕셔너리 내의 'fin_prdt_nm'의 값이야. " }
        )
    if '적금' in input_message and '추천' in input_message:
        chat_history.append(
            {"role": "system", "content": f"만약 적금 상품을 추천한다면 아래 정보에 기반해서 적금 상품의 이름과 함께 정보를 한글로 답변해줘. {installment_info} 적금 상품의 이름은 각 딕셔너리 내의 'fin_prdt_nm'의 값이야."}
        )
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            temperature=0.0,
            # response_format={'type':'json_object'},
            messages= chat_history,
            stop=['Human'],
            frequency_penalty=0.5,
            presence_penalty=0.5
        )
        output_message = response.choices[0].message.content
        print(output_message)
        chat_history.append({"role": "assistant", "content": f"{output_message}"})
        return Response(output_message,status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def history_initialize(request):
    global chat_history
    chat_history = []
    return Response(status=status.HTTP_202_ACCEPTED)
