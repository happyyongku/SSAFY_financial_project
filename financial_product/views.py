from django.shortcuts import render
import requests
# Create your views here.

def get_data(request):
    page_no = list(range(10))
    