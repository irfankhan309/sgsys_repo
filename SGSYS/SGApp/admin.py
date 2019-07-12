from django.contrib import admin
from SGApp.models import AClist,Buy,Quotation


class ACadmin(admin.ModelAdmin):
    list_display = ['Image','Info','Rating']

class BuyAdmin(admin.ModelAdmin):
    list_display =['Name','Phone','Address']


class QuoatationAdmin(admin.ModelAdmin):
    list_display =['Brand','Tons','Phone','Email','Query']


admin.site.register(AClist,ACadmin)
admin.site.register(Buy,BuyAdmin)
admin.site.register(Quotation,QuoatationAdmin)
