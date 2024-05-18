from django.db import models

# Create your models here.

class FinancialCompany(models.Model):
    kor_co_nm = models.CharField(max_length=50) # 금융회사명
    fin_co_no = models.TextField()   # 금융회사 코드

class DepositProduct(models.Model):
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    kor_co_nm = models.TextField()
    fin_prdt_cd = models.TextField()
    fin_prdt_nm = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_member = models.TextField()
    max_limit = models.BigIntegerField(null=True)
    etc_note = models.TextField()
    
class DepositOption(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    intr_rate_type = models.CharField(max_length=10)
    intr_rate_type_nm = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    dcls_month = models.CharField(max_length=10)
    
class InstallmentSavingProduct(models.Model):
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    kor_co_nm = models.TextField()
    fin_prdt_cd = models.TextField()
    fin_prdt_nm = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_member = models.TextField()
    max_limit = models.BigIntegerField(null=True)
    etc_note = models.TextField()
    
class InstallmentSavingOption(models.Model):
    fin_prdt_cd = models.ForeignKey(InstallmentSavingProduct, on_delete=models.CASCADE)
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    intr_rate_type = models.CharField(max_length=10)
    intr_rate_type_nm = models.TextField()
    rsrv_type = models.CharField(max_length=10)
    rsrv_type_nm = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    dcls_month = models.CharField(max_length=10)
    
class PensionProduct(models.Model):
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    fin_prdt_nm = models.TextField()
    join_way = models.TextField(null=True)
    pnsn_kind = models.CharField(max_length=10)
    pnsn_kind_nm = models.TextField()
    prdt_type = models.CharField(max_length=10)
    prdt_type_nm = models.TextField()
    avg_prft_rate = models.FloatField()
    btrm_prft_rate_1 = models.FloatField(null=True)
    btrm_prft_rate_2 = models.FloatField(null=True)
    btrm_prft_rate_3 = models.FloatField(null=True)
    sale_co = models.TextField()
    etc = models.TextField(null=True)
    
class PensionOption(models.Model):
    fin_prdt_cd = models.ForeignKey(PensionProduct, on_delete=models.CASCADE)
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    pnsn_recp_trm = models.CharField(max_length=30)
    pnsn_recp_trm_nm = models.CharField(max_length=30)
    pnsn_entr_age = models.CharField(max_length=30)
    pnsn_entr_age_nm = models.CharField(max_length=30)
    mon_paym_atm = models.CharField(max_length=30)
    mon_paym_atm_nm = models.CharField(max_length=30)
    paym_prd = models.CharField(max_length=30)
    paym_prd_nm = models.CharField(max_length=30)
    pnsn_strt_age = models.CharField(max_length=30)
    pnsn_strt_age_nm = models.CharField(max_length=30)
    pnsn_recp_amt = models.IntegerField()
    dcls_month = models.CharField(max_length=10)
    
class ExchangRate(models.Model):
    date = models.DateField(auto_now_add=True)
    cur_unit = models.CharField(max_length=10)
    cur_nm = models.CharField(max_length=30)
    ttb = models.FloatField()
    tts = models.FloatField()
    deal_bas_r = models.FloatField()
    