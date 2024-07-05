from rest_framework import serializers
from .models import (
    FinancialCompany, 
    DepositOption, 
    DepositProduct, 
    InstallmentSavingOption,
    InstallmentSavingProduct,
    ExchangRate
    )

class FinancialCompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=FinancialCompany
        fields='__all__'
        
class DepositProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=DepositProduct
        fields='__all__'
        
class DepositOptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=DepositOption
        fields='__all__'
        
class InstallmentSavingProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=InstallmentSavingProduct
        fields='__all__'
        
class InstallmentSavingOptionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=InstallmentSavingOption
        fields='__all__'
        
        
class ExchangeRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=ExchangRate
        fields='__all__'