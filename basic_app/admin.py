from django.contrib import admin

from . import inspectDB_models

# Register your models here.
admin.site.register(inspectDB_models.Anketa)
admin.site.register(inspectDB_models.AuthUser)
admin.site.register(inspectDB_models.Users)
