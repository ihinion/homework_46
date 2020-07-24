from django.contrib import admin
from webapp.models import Task

# superuser
# login: admin
# password: admin
admin.site.register(Task)
