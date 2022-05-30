from django.contrib import admin

from .models import *


# Register your models here.
class FacilityManagementClientCompanyAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'company_name',
                    'company_identity_code',
                    'company_order_password',
                    'address',
                    'contact',
                    'email',
                    'date_added'
                    )

    search_fields = ('id',
                     'company_name',
                     'company_identity_code',
                     'company_order_password',
                     'address',
                     'contact',
                     'email',
                     'date_added'
                     )


    list_filter = (
                     'company_name',
                     'date_added'
                     )

class MainCarosedis(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'img',
                    'date_added'
                    )

    search_fields = ('id',
                     'name',
                     'img',
                     'date_added'
                     )


class FacilityManagemetSevicesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'services_name',
        'img',
        'about_service',
        'date_added'
    )
    search_fields = (
        'id',
        'services_name',
        'img',
        'about_service',
        'date_added'
    )


class FacilityManagementCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Facility_cate_name',
        'date_added'
    )

    search_fields = (
        'id',
        'Facility_cate_name',
        'date_added'
    )


class FacilityManagementItemAdmin(admin.ModelAdmin):
    list_display = (
            'item_cat' ,
             'item_name',
                'price_per_a_quantity_bought',
                'stocks',
                'price_being_sold_for',
                'about_item' ,
                'date_added' )
    search_fields =  (
            'item_cat' ,
             'item_name',
                'price_per_a_quantity_bought',
                'stocks',
                'price_being_sold_for',
                'about_item' ,
                'date_added' )
    list_filter = (
              'item_cat' ,
                    'date_added' )

class FacilityManagementClientsAdmin(admin.ModelAdmin):
    list_display = (
    'category' ,
    'company_name',
    'company_identity_code' ,
    'email' ,
    'client_login_address' ,
    'contact',
    'date_time_login',
    'date_time_logout',
    )

    search_fields = (
    'category' ,
    'company_name',
    'company_identity_code' ,
    'email' ,
    'client_login_address',
    'contact',
    'date_time_login',
    'date_time_logout',

    )

    list_filter = ('category' ,
    'date_time_login',
     'date_time_logout'
                   )

class FacilityManagementOrder(admin.ModelAdmin):
    list_display = (
        'cust_name',
        'category',
    'datetime_local' ,
    # ___________________________
    'option1' ,
    'quantity1',
    # ____________________
    'option2' ,
    'quantity2' ,
    # _______________________
    'option3' ,
    'quantity3',
    # _______________________
    'option4',
    'quantity4' ,
    # _______________________
    'option5',
    'quantity5',
    # _______________________
    'option6' ,
    'quantity6',
    # _______________________
    'option7',
    'quantity7',
    # _______________________
    'option8' ,
    'quantity8' ,
    # _______________________
    'option9',
    'quantity9',
    # _______________________
    'option10' ,
    'quantity10' ,
    # _______________________
    'companyorderpassword',
    'message',
    'read',
    'order_done',
    'date_added'
    )
search_fields = (
      'cust_name',
    'category',
    'datetime_local' ,
    # ___________________________
    'option1' ,
    'quantity1',
    # ____________________
    'option2' ,
    'quantity2' ,
    # _______________________
    'option3' ,
    'quantity3',
    # _______________________
    'option4',
    'quantity4' ,
    # _______________________
    'option5',
    'quantity5',
    # _______________________
    'option6' ,
    'quantity6',
    # _______________________
    'option7',
    'quantity7',
    # _______________________
    'option8' ,
    'quantity8' ,
    # _______________________
    'option9',
    'quantity9',
    # _______________________
    'option10' ,
    'quantity10' ,
    # _______________________
    'companyorderpassword',
    'message',
      'read',
      'order_done',
      'date_added'
    )
list_filter = ('cust_name',
               'category',
               'read',
               'order_done',
               'date_added')

admin.site.register(facility_management_order,FacilityManagementOrder)
admin.site.register(facility_management_clients_login,FacilityManagementClientsAdmin)
admin.site.register(facilty_management_item, FacilityManagementItemAdmin)
admin.site.register(facilty_management_category, FacilityManagementCategoryAdmin)
admin.site.register(facility_management_service, FacilityManagemetSevicesAdmin)
admin.site.register(facility_management_client, FacilityManagementClientCompanyAdmin)
admin.site.register(facility_maincarodis, MainCarosedis)
