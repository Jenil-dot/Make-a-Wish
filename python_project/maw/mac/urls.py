"""mac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/' , include('shop.urls')),
    path('', views.index, name="ShopHome"),
    path('shop/' , include('shop.urls')),
    path("contact/", views.contact, name="ContactUs"), 
    path("login/",views.login, name="Login"), 
    path("signup/",views.signup, name="SignUp"),
    path('date/' , views.date),
    path('birthdayboy/' , views.birthdayboy),
    path('whoisuser/' , views.whoisuser),
    path('whoisuser1/' , views.whoisuser1),
    path('display/',views.display),
    path("birthview/",views.birthview),
    path("wedding/",views.wedding),
    path("greduate/",views.greduate),
    path("greduatedate/",views.greduatedate),
    path("whoisuser2/",views.whoisuser2),
    path("greduationgdata/",views.greduationgdata),
    path("weddingdate/",views.weddingdate),
    path("weddinginfo/",views.weddinginfo),
    path("ss/",views.ss),
    path("user1/",views.user1),
    path("user/",views.user),
    path("contact1/",views.contact1),
    path("logout/",views.logout),
    #path("post/",views.post),

    path('posts/', include('apps.posts.urls')),
    
 #path('n1/',views.n1),
   #path('blog/' , include('blog.urls'))
    #path('index/',views.index),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


