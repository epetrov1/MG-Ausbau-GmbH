from django.contrib import admin
from . models import Service
from django_summernote.admin import SummernoteModelAdmin



class ServicePostAdmin(SummernoteModelAdmin):  
    exclude = ('slug',)
    list_display = ('title',)
    summernote_fields = ('description', 'description_de', 'description_en')

admin.site.register(Service, ServicePostAdmin)