from django.db import models

# Create your models here.

class FinancialCompany(models.Model):
    kor_co_nm = models.CharField(max_length=20) # 금융회사명
    fin_co_no = models.TextField()   # 금융회사 코드

class DepositProduct(models.Model):
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    fin_prdt_nm = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_member = models.TextField()
    max_limit = models.IntegerField()
    etc_note = models.TextField()
    
class DepositOption(models.Model):
    fin_prdt_cd = models.ForeignKey(DepositProduct, on_delete=models.CASCADE)
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    intr_rate_type = models.CharField(max_length=10)
    intr_rate_type_nm = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    
class InstallmentSavingProduct(models.Model):
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    fin_prdt_nm = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_member = models.TextField()
    max_limit = models.IntegerField()
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
    
class PensionProduct(models.Model):
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    fin_prdt_nm = models.TextField()
    pnsn_kind = models.CharField(max_length=10)
    pnsn_kind_nm = models.TextField()
    prdt_type = models.CharField(max_length=10)
    prdt_type_nm = models.TextField()
    dcls_rate = models.FloatField()
    guar_rate = models.FloatField()
    etc = models.TextField()
    
class PensionOption(models.Model):
    fin_prdt_cd = models.ForeignKey(PensionProduct, on_delete=models.CASCADE)
    fin_co_no = models.ForeignKey(FinancialCompany, on_delete=models.CASCADE)
    intr_rate_type = models.CharField(max_length=10)
    intr_rate_type_nm = models.TextField()
    rsrv_type = models.CharField(max_length=10)
    rsrv_type_nm = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()