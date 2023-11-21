from django.urls import path
from main.views import create_product_flutter, show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, adding_amount, removing_amount, deleting_amount
from main.views import register, login_user, logout_user, edit_item, get_product_json, add_product_ajax, add_amount_ajax, remove_amount_ajax, delete_item_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add/<int:id>', adding_amount, name='add'),
    path('remove/<int:id>', removing_amount, name='remove'),
    path('delete/<int:id>', deleting_amount, name='delete'),
    path('edit-itemt/<int:id>', edit_item, name='edit_item'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('add/', add_amount_ajax, name='add'),
    path('remove/', remove_amount_ajax, name='remove'),
    path('delete/', delete_item_ajax, name='delete'), 
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]