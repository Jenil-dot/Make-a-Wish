from django.contrib import admin
from django.urls import include ,path
from shop import views

urlpatterns = [

	path('admin/', admin.site.urls),
    path('', views.index, name="ShopHome"),
	path("about/", views.about, name="AboutUs"), 
	path("contact/", views.contact, name="ContactUs"),  
	path("login/",views.login, name="Login"),
	path("signup/",views.signup, name="SignUp"),
	path("date/",views.date),
	path("birthdayboy/",views.birthdayboy),
	path("whoisuser/",views.whoisuser),
	path("next/",views.next),
	path("n1/",views.n1),
	path("whoisuser1/",views.whoisuser1),
	path("display/",views.display),
	path("birthview/",views.birthview),
	path("wedding/",views.wedding),
	path("weddingdate/",views.weddingdate),
	path("greduate/",views.greduate),
	path("greduatedate/",views.greduatedate),
	path("whoisuser2/",views.whoisuser2),
    path("greduationgdata/",views.greduationgdata),
    path("weddinginfo/",views.weddinginfo),
    path("ss/",views.ss),
    path("user/",views.user),
    path("user1/",views.user1),
    path("contact1/",views.contact1),
    path("logout/",views.logout),
    #path("post/",views.post),
   
]



  