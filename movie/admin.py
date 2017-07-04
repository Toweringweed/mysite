from django.contrib import admin
from .models import Mdetail, Mclass, Mtag, Myear, Marea, Martist

class AdminStyle(admin.ModelAdmin):
    list_display = ('m_name', 'm_class', 'm_year', 'm_download', 'm_update')
admin.site.register(Mdetail, AdminStyle)
admin.site.register(Mclass)
admin.site.register(Myear)
admin.site.register(Martist)
admin.site.register(Marea)
admin.site.register(Mtag)

