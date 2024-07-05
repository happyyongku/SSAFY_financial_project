# Django 폴더 별 설명

## 앱 폴더 내 .py 파일
- models.py
    - DB 설계
    - ERD 설계 이후 models.py에서 해당 DB를 설계
    - ex) models.Charfield(max_length=10) : 문자열 필드, 최대 10자

- serializers.py
    - 직렬화 코드

- views.py
    - 내부 동작 함수 코드

- urls.py
    - 요청받은 url에 따라 views.py 내의 함수로 연결

## account
- 계정 관리 앱

## financial_product
- 금융 상품 관리 앱

## financial_project
- 프로젝트 폴더
