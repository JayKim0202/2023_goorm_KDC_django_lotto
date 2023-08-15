from django.contrib import admin
from .models import GuessNumbers    # 현 폴더와 동일한 폴더에 위치했을 경우 현 폴더 생략 가능
# from lotto.models import GuessNumbers

# Register your models here.
admin.site.register(GuessNumbers)
