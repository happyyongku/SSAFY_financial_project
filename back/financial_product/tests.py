from django.test import TestCase
from django.conf import settings

# Create your tests here.
import json
import pymysql
import pandas as pd


conn = pymysql.connect(
    host='localhost',
    user='yonggu97',
    password = settings.DB_PASSWORD,
    db = 'ssafy_final'
)

cursor = conn.cursor()

