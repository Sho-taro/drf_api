from django.contrib import admin
from  .models import Task

# Register your models here.
admin.site.register(Task)    # Taskモデル（テーブル）をadminツールで操作できるように登録