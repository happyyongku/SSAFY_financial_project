from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.

@api_view(['GET','POST'])
def login(request):
    if request.mehtod == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            context = {
                'login' : True
            }                              # 추후에 True, False 말고 쿠키 데이터를 보내는 것으로 변경해야 함
            return Response(context)
        context = {
            'login' : False
        }
        return Response(context)
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout(request):
    auth_logout(request)
    context = {
        'logout' : True
    }
    return Response(context)