import os
import django

# Django 프로젝트 설정 로드
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")  # 'myproject'를 실제 프로젝트 이름으로 변경하세요.
django.setup()

from main.models import Category  
category_names = [
    "Building1", "Building2", "Building3", "Building4", "Building5",
    "Building6", "Building7", "Building8", "Building9", "Building10",
    "Building11", "Building12", "Building13", "Building14", "Building15"
]

# 카테고리 생성
for name in category_names:
    Category.objects.create(name=name)

print("Categories added succpyessfully!")
