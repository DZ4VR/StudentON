from django.contrib import admin
from .models import aboutPageContent
from .models import homePageContent
from .models import Articles

class aboutPageContentAdmin(admin.ModelAdmin):
    list_filter = ['id']

class homePageContentAdmin(admin.ModelAdmin):
    list_filter = ['id']

admin.site.register(aboutPageContent , aboutPageContentAdmin)
admin.site.register(homePageContent , homePageContentAdmin)



class ArticleAdmin(admin.ModelAdmin):
    list_filter = ['date']

admin.site.register(Articles , ArticleAdmin)