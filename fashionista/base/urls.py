from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name="home"),
    path('products/<str:category>/',views.viewmore,name="viewmore"),
    path('services/<str:slug>/',views.services_details,name="services_detail"),
   
    
    


    
    path('WhySoi/',views.whybeele,name="whywe"),
    
    path('contact/',views.contact,name="contact"),
    path('messageconfirmation/',views.support,name="messageconfirmation"),
    

   
 ]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)