from django.urls import path 
from . import views
# image
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.login_form,name='login_form'),
    
    path('reg/',views.reg_form,name='reg_form'),
    path('Prod_form/',views.prod_form,name='pro_form'),
    path('view_product/',views.view_product,name='view_product'),
    path('index/',views.index,name="index_page"),
    path('cart/',views.cart_page,name='cart'),
    path('products',views.card,name='products'),
    path('add_to_cart/ <int:i>',views.add_to_cart,name='cartpage'),
    path('delete_cartitem/ <int:item_id>',views.delete_cart,name='delete_cart'),
    path('delete_all_item/',views.delete_all_items,name='delete_all'),
    path('logout/',views.userlogout,name='logout'),
    
]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

