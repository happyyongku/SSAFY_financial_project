from django.db import models
from django.conf import settings
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
    intr_rate_type_nm = models.CharField(max_length=20, blank=True)
    rate_1 = models.FloatField(blank=True, null=True)
    rate_3 = models.FloatField(blank=True, null=True)
    rate_6 = models.FloatField(blank=True, null=True)
    rate_12 = models.FloatField(blank=True, null=True)
    rate_24 = models.FloatField(blank=True, null=True)
    rate_36 = models.FloatField(blank=True, null=True)
    rate_1_p = models.FloatField(blank=True, null=True)
    rate_3_p = models.FloatField(blank=True, null=True)
    rate_6_p = models.FloatField(blank=True, null=True)
    rate_12_p = models.FloatField(blank=True, null=True)
    rate_24_p = models.FloatField(blank=True, null=True)
    rate_36_p = models.FloatField(blank=True, null=True)
    joined_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='user_deposit',
        symmetrical=True,
        blank=True,
        null=True
        )
    
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
    intr_rate_type_nm = models.CharField(max_length=20, blank=True)
    rate_1 = models.FloatField(blank=True, null=True)
    rate_3 = models.FloatField(blank=True, null=True)
    rate_6 = models.FloatField(blank=True, null=True)
    rate_12 = models.FloatField(blank=True, null=True)
    rate_24 = models.FloatField(blank=True, null=True)
    rate_36 = models.FloatField(blank=True, null=True)
    rate_1_p = models.FloatField(blank=True, null=True)
    rate_3_p = models.FloatField(blank=True, null=True)
    rate_6_p = models.FloatField(blank=True, null=True)
    rate_12_p = models.FloatField(blank=True, null=True)
    rate_24_p = models.FloatField(blank=True, null=True)
    rate_36_p = models.FloatField(blank=True, null=True)
    joined_user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='user_installment',
        symmetrical=True,
        blank=True,
        null=True
        )
    
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
    
    
class ExchangRate(models.Model):
    date = models.DateField()
    cur_unit = models.CharField(max_length=10)
    cur_nm = models.CharField(max_length=30)
    ttb = models.FloatField()
    tts = models.FloatField()
    deal_bas_r = models.FloatField()
    