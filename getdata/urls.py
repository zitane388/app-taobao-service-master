# -*- coding: utf-8 -*-

from django.urls import path

from . import views
urlpatterns = [
    path('login',views.login,name="login"),
    path('prohibition',views.prohibition,name="prohibition"),
    path('setting_save',views.setting_save,name="setting_save"),
    path('naver_all_upload',views.naver_all_upload,name="naver_all_upload"),
    path('naver_page',views.naver_page,name="naver_page"),
    path('sourcing_upload',views.sourcing_upload,name="sourcing_upload"),
    path('sourcing_page',views.sourcing_page,name="sourcing_page"),
    path('sourcing_product_upload',views.sourcing_product_upload,name="sourcing_product_upload"),
    path('sourcing_product_confirm',views.sourcing_product_confirm,name="sourcing_product_confirm"),
    path('sourcing_product_delete',views.sourcing_product_delete,name="sourcing_product_delete"),
    path('sourcing_update',views.sourcing_update,name="sourcing_update"),
    path('sourcing_delect',views.sourcing_delect,name="sourcing_delect"),
    path('problem_set',views.problem_set,name="problem_set"),
    path('manager_update',views.manager_update,name="manager_update"),
    path('prohibition_list_get',views.prohibition_list_get,name="prohibition_list_get"),
    path('seller_up_load',views.seller_up_load,name="seller_up_load"),
    path('naver_all_delete',views.naver_all_delete,name="naver_all_delete"),
    path('activation',views.activation,name="activation"),
    path('set_item_id',views.set_item_id,name="set_item_id"),
    path('get_option_data',views.get_option_data,name="get_option_data"),
    path('option_upload',views.option_upload,name="option_upload")
    
]
