from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# 設置 Django 默認設置模塊
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_iot.project_iot.settings')

app = Celery('project_iot')

# 使用字符串保證 worker 可以序列化任務對象
# 命名空間 'CELERY' 表示所有與 celery 相關的配置鍵應該是大寫
app.config_from_object('django.conf:settings', namespace='CELERY')


# 自動發現異步任務
app.autodiscover_tasks()

# 測試
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')