from django.contrib import admin


#admin.site.register(HomePage)

from django_summernote.admin import SummernoteModelAdmin
from .models import HomePage

class HomeAboutAdmin(SummernoteModelAdmin):
    exclude = ('preporyka1', 'preporyka2', 'preporyka3',)
    list_display = ('header',)
    summernote_fields = ('about_us', 'about_us_de', 'about_us_en')

admin.site.register(HomePage, HomeAboutAdmin)