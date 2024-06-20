import os
import django

# Django 프로젝트 설정 로드
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")  # 'project'를 실제 프로젝트 이름으로 변경하세요.
django.setup()

from main.models import Category

# 기존 데이터 삭제
Category.objects.all().delete()

# 새로운 카테고리 이름 리스트
subcategory_names = [
    "대운동장", "사회과학관", "혜화관", "학술문화관", "명진관",
    "신공학관", "중앙도서관", "상록원", "팔정도", "법학관",
    "정보문화관", "만해광장", "학생회관", "학림관", "원흥관"
]

maincategory_names =[
    'a','a','a','a','b','b','b','b','b','b','c','c','c','c','c',
]

# 카테고리 생성
for subcategory, maincategory in zip(subcategory_names, maincategory_names):
    Category.objects.create(subcategory=subcategory, maincategory=maincategory)

print("Categories updated successfully!")
