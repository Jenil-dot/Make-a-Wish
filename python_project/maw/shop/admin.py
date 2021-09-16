from django.contrib import admin
from shop.models import *
# Register your models here.


class contactadmin(admin.ModelAdmin):
    list_display=['name','email' ,'phone']
    list_filter=['name','email', 'phone']


class useradmin(admin.ModelAdmin):
    list_display=['fname','lname' ,'email']
    list_filter=['fname','lname' ,'email']


'''class MyModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}
admin.site.register(User, MyModelAdmin)

class MyModelAdmin1(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

admin.site.register(Contact, MyModelAdmin1)'''




admin.site.register(Contact,contactadmin)
admin.site.register(User,useradmin)
#admin.site.register(Contact)
#admin.site.register(User)
#admin.site.register(Birthday)
#admin.site.register(userModel)
#admin.site.register(Contact)
admin.site.register(image)
admin.site.register(birth)
admin.site.register(weds)
admin.site.register(greduation)
admin.site.register(User1)




