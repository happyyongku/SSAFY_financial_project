from rest_framework import serializers
from django.conf import settings
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from django.contrib.auth import get_user_model


User = settings.AUTH_USER_MODEL
UserModel = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    nickname=serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=30
    )
    capital=serializers.IntegerField(
        required=False,
        default=0
    )
    special_condition=serializers.CharField(
        required=False,
        allow_blank=True,
    )
    
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username',''),
            'password': self.validated_data.get('password1',''),
            'nickname': self.validated_data.get('nickname',''),
            'email': self.validated_data.get('email',''),
            'birth': self.validated_data.get('birth',''),
            'capital': self.validated_data.get('capital',''),
            'special_condition': self.validated_data.get('special_condition','')
        }
        
class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        extra_fields = []
        
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        if hasattr(UserModel, 'first_name'):
            extra_fields.append('first_name')
        if hasattr(UserModel, 'last_name'):
            extra_fields.append('last_name')
        if hasattr(UserModel, 'nickname'):
            extra_fields.append('nickname')    
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email',)
        
class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = (
            'id', 
            'username', 
            'password', 
            'first_name', 
            'last_name',
            'email',
            'nickname',
            'capital',
            'special_condition',
            )
        
class UserProfileEditSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 
            'last_name',
            'email',
            'nickname',
            'capital',
            'special_condition',
            )
    # def save(self, **kwargs):
    #     # 인스턴스를 가져오기 위해 validated_data 사용
    #     instance = kwargs.pop('instance', None)
    #     # 인스턴스가 존재하는 경우
    #     if instance is not None:
    #         for attr, value in self.validated_data.items():
    #             setattr(instance, attr, value)
    #         instance.save()  # 모델 인스턴스의 save() 메소드 호출
    #         return instance
    #     else:
    #         return super().save(**kwargs)