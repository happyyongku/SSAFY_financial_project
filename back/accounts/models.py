from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter

# Create your models here.

class User(AbstractUser):
    nickname=models.CharField(max_length=30, blank=True, null=True, default='anonymous')
    # birth = models.DateField(blank=True)
    capital = models.BigIntegerField(blank=True, null=True)
    special_condition = models.TextField(blank=True, null=True)
    # super.username.set_attributes_from_name('editible', False)
    

# # class UserProfile(models.Model):
# #     user_pk = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
# #     birth = models.DateField()
# #     capital = models.BigIntegerField()

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        # nickname 필드를 추가
        nickname = data.get("nickname")
        # birth = data.get("birth")
        capital = data.get("capital")
        special_condition = data.get("special_condition")
        
        user_email(user, email)
        user_username(user, username)
        
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if "password" in data:
            user.set_password(data["password"])
            
        if capital:
            user_field(user, "capital", capital)
        if special_condition:
            user_field(user, "special_condition", special_condition)
        # if birth:
        #     user_field(user, "birth", birth)
        # else:
        #     user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user