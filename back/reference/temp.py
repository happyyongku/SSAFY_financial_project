# ---------------------------------- 연금 저축 ----------------------------------
        # if idx == 2:
        #     for GrpNo in ['050000', '060000']:
        #         params_request[idx]['topFinGrpNo'] = GrpNo
        #         page = 1
        #         while True:
        #             params_request[idx]['pageNo'] = page
        #             page += 1
        #             response = requests.get(url, params=params_request[idx]).json()['result']
        #             if response['max_page_no'] < response['now_page_no']:
        #                 break
        #             test_data = response
        #             for product in response['baseList']:
        #                 fin_cd = product['fin_co_no']
        #                 company_data = {
        #                     'kor_co_nm': product['kor_co_nm'],
        #                     'fin_co_no': product['fin_co_no']
        #                 }

        #                 company, created = FinancialCompany.objects.update_or_create(
        #                     fin_co_no=fin_cd,
        #                     defaults=company_data
        #                 )

                        
        #                 p_product_data = {
        #                     'fin_co_no': company,  # ForeignKey relationship
        #                     'fin_prdt_cd': product['fin_prdt_cd'],
        #                     'fin_prdt_nm': product['fin_prdt_nm'],
        #                     'join_way': product['join_way'],
        #                     'pnsn_kind': product['pnsn_kind'],
        #                     'pnsn_kind_nm': product['pnsn_kind_nm'],
        #                     'prdt_type': product['prdt_type'],
        #                     'prdt_type_nm': product['prdt_type_nm'],
        #                     'avg_prft_rate': product['avg_prft_rate'],
        #                     'btrm_prft_rate_1': product['btrm_prft_rate_1'],
        #                     'btrm_prft_rate_2': product['btrm_prft_rate_2'],
        #                     'btrm_prft_rate_3': product['btrm_prft_rate_3'],
        #                     'etc': product['etc'],
        #                 }
        #                 try:
        #                     PensionProduct.objects.update_or_create(
        #                         fin_co_no=company,
        #                         fin_prdt_cd=product['fin_prdt_cd'],
        #                         defaults=p_product_data
        #                 )
        #                 except:
        #                     continue
                        
        #             for option in response['optionList']:
        #                 company_pnsn_opt = FinancialCompany.objects.get(fin_co_no=option['fin_co_no'])
        #                 product_pnsn_opt = PensionProduct.objects.get(
        #                     fin_prdt_cd=option['fin_prdt_cd'], 
        #                     fin_co_no=company_pnsn_opt
        #                     )
                        
        #                 p_option_data = {
        #                     'fin_prdt_cd': product_pnsn_opt,
        #                     'fin_co_no': company_pnsn_opt,
        #                     'pnsn_recp_trm': option['pnsn_recp_trm'],
        #                     'pnsn_recp_trm_nm': option['pnsn_recp_trm_nm'],
        #                     'pnsn_entr_age': option['pnsn_entr_age'],
        #                     'pnsn_entr_age_nm': option['pnsn_entr_age_nm'],
        #                     'mon_paym_atm': option['mon_paym_atm'],
        #                     'mon_paym_atm_nm': option['mon_paym_atm_nm'],
        #                     'paym_prd': option['paym_prd'],
        #                     'paym_prd_nm': option['paym_prd_nm'],
        #                     'pnsn_strt_age': option['pnsn_strt_age'],
        #                     'pnsn_strt_age_nm': option['pnsn_strt_age_nm'],
        #                     'pnsn_recp_amt': option['pnsn_recp_amt'],
        #                     'dcls_month': option['dcls_month']
        #                 }
        #                 try:
        #                     PensionOption.objects.update_or_create(
        #                         fin_prdt_cd = product_pnsn_opt,
        #                         dcls_month=company_pnsn_opt,
        #                         defaults=p_option_data
        #                 )
        #                 except:
        #                     continue
                    