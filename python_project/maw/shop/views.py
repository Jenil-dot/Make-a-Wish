from django.shortcuts import render,redirect
from django.http import HttpResponse
from shop.models import *
#for landing page
def index(request):
    #return HttpResponse(" Index Shop ")
    return render(request, 'index.html')

# for about us page
def about(request):
    if 'username' in request.session:
        return render(request,'about.html',{'username':request.session['username']})
    return render(request,'index.html')


# for contact us page

def contact1(request):
    if 'username' in request.session:
        return render(request,'contact.html',{'username':request.session['username']})
    return render(request,'index.html')
    #return render(request,'contact.html')
    


'''def contact(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    desc = request.GET.get('desc')
    data=Contact()
    data.name=name
    data.email=email
    data.phone=phone
    data.desc=desc
    data.save()
    return render(request,"contact.html")'''

def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})


# for login page
def login(request):
    return render(request,'login.html')

def user(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    repeat = request.POST.get('repeat')
    
    data=User()
    data.fname=fname
    data.lname=lname
    data.email=email
    data.password=password
    data.repeat=repeat

    data.save()
    return render(request,"login.html")


def user1(request):
    name=request.POST.get('name')
    password=request.POST.get('password')
    data=User.objects.all()
    for i in data:
        if i.fname == name  and i.password == password:
            request.session['username']=i.fname
            return render(request,'index.html')
    return render(request,'index.html') 
    
# for signup page
def signup(request):
    '''if 'username' in request.session:
        return render(request,'signup.html')
    return render(request,'index.html')'''
    return render(request,'signup.html')
   

'''def user(request):

    thank = False   
    if request.method=="POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        repeat = request.POST.get('repeat', '')
        user = User(fname=fname, lname=lname, email=email, password=password, repeat=repeat)
        user.save()
        thank = True
    return render(request, 'whoisuser.html', {'thank': thank})'''

# for date page
def date(request):
    if 'username' in request.session:
        return render(request,'date.html',{'username':request.session['username']})
    return render(request,'index.html')
    #return render(request,"date.html")

# for birthdayboy page
def birthdayboy(request):
    if 'username' in request.session:
        return render(request,'birthdayboy.html',{'username':request.session['username']})
    return render(request,'index.html')
    #return render(request,'birthdayboy.html')
    

#for who is user page
def whoisuser(request):
    if 'username' in request.session:
        return render(request,'whoisuser.html',{'username':request.session['username']})
    return render(request,'index.html')
    #return render(request,'whoisuser.html')

# for next page (redirect)

def next(request):
    return redirect('/birthdayboy/')

def n1(request):
    return redirect('/date/')

# display page
def display(request):
    img=image.objects.all()
    return render(request,'display.html',{"images":img})


# for birthday models
def birthview(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    address2 = request.POST.get('address2')
    city=request.POST.get('city')
    data=birth()
    data.name=name
    data.email=email
    data.address=address
    data.address2=address2
    data.city=city
    data.save()
    return render(request,"birthdayboy.html")

def whoisuser1(request):
    if 'username' in request.session:
        return render(request,'whoisuser1.html',{'username':request.session['username']})
    return render(request,'index.html')
    #return render(request,'whoisuser1.html')

# for wedding  
def wedding(request):
    if 'username' in request.session:
        return render(request,'wedding.html',{'username':request.session['username']})
    return render(request,'index.html')
    #return render(request,'wedding.html')

def weddingdate(request):
    if 'username' in request.session:
        return render(request,'weddingdate.html',{'username':request.session['username']})
    return render(request,'index.html')
    #return render(request,'weddingdate.html')

def weddinginfo(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    address2 = request.POST.get('address2')
    city=request.POST.get('city')
    data=weds()
    data.name=name
    data.email=email
    data.address=address
    data.address2=address2
    data.city=city
    data.save()
    return render(request,"wedding.html")

def whoisuser2(request):
    if 'username' in request.session:
        return render(request,'whoisuser2.html',{'username':request.session['username']})
    return render(request,'index.html')
    #return render(request,'whoisuser2.html')

#for graduation
def greduate(request):
    if 'username' in request.session:
        return render(request,'greduate.html',{'username':request.session['username']})
    return render(request,'index.html')

    #return render(request,'greduate.html')

def greduatedate(request):
    if 'username' in request.session:
        return render(request,'greduatedate.html',{'username':request.session['username']})
    return render(request,'index.html')
    #return render(request,'greduatedate.html')
    
def greduationgdata(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    address2 = request.POST.get('address2')
    city=request.POST.get('city')
    data=greduation()
    data.name=name
    data.email=email
    data.address=address
    data.address2=address2
    data.city=city
    data.save()
    return render(request,'greduate.html')


def ss(request):
    return render(request,'ss.html')


def logout(request):
    del request.session['username']
    return render(request,'index.html')

'''def post(request):
    return render(request,'posts/post_list.html')'''

# Create your views here.
'''
#for landing page
def index(request):
    #return HttpResponse(" Index Shop ")
    return render(request, 'index.html')

# for about us page
def about(request):
    if 'username' in request.session:
        return render(request,'about.html')
    return render(request,'index.html')


# for contact us page

def contact1(request):
    if 'username' in request.session:
        return render(request,'contact.html')
    return render(request,'index.html')'''
    


'''def contact(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    desc = request.GET.get('desc')
    data=Contact()
    data.name=name
    data.email=email
    data.phone=phone
    data.desc=desc
    data.save()
    return render(request,"contact.html")'''

'''def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})


# for login page
def login(request):
    return render(request,'login.html')

def user(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    repeat = request.POST.get('repeat')
    
    data=User()
    data.fname=fname
    data.lname=lname
    data.email=email
    data.password=password
    data.repeat=repeat

    data.save()
    return render(request,"login.html")


def user1(request):
    name=request.POST.get('name')
    password=request.POST.get('password')
    data=User.objects.all()
    for i in data:
        if i.fname == name  and i.password == password:
            request.session['username']=i.fname
            return render(request,'signup.html')
    return render(request,'index.html') 
    
# for signup page
def signup(request):
    if 'username' in request.session:
        return render(request,'signup.html')
    return render(request,'index.html')'''
   

'''def user(request):

    thank = False   
    if request.method=="POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        repeat = request.POST.get('repeat', '')
        user = User(fname=fname, lname=lname, email=email, password=password, repeat=repeat)
        user.save()
        thank = True
    return render(request, 'whoisuser.html', {'thank': thank})'''

# for date page
'''def date(request):
    return render(request,"date.html")

# for birthdayboy page
def birthdayboy(request):
    if 'username' in request.session:
        return render(request,'birthdayboy.html')
    return render(request,'index.html')
    

#for who is user page
def whoisuser(request):
    if 'username' in request.session:
        return render(request,'whoisuser.html')
    return render(request,'index.html')
    #return render(request,'whoisuser.html')
# for next page (redirect)
def next(request):
    return redirect('/birthdayboy/')

def n1(request):
    return redirect('/date/')
# display page
def display(request):
    img=image.objects.all()
    return render(request,'display.html',{"images":img})'''

'''def save(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    address2 = request.POST.get('address2')
    city=request.POST.get('city')
    data=birthday()
    data.name=name
    data.email=email
    data.address=address
    data.address2=address2
    data.city=city
    data.save()
    return render(request,"birthdayboy.html")'''

# for birthday models
'''def birthview(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    address2 = request.POST.get('address2')
    city=request.POST.get('city')
    data=birth()
    data.name=name
    data.email=email
    data.address=address
    data.address2=address2
    data.city=city
    data.save()
    return render(request,"birthdayboy.html")

def whoisuser1(request):
    return render(request,'whoisuser1.html')

# for wedding  
def wedding(request):
    return render(request,'wedding.html')

def weddingdate(request):
    return render(request,'weddingdate.html')

def weddinginfo(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    address2 = request.POST.get('address2')
    city=request.POST.get('city')
    data=weds()
    data.name=name
    data.email=email
    data.address=address
    data.address2=address2
    data.city=city
    data.save()
    return render(request,"wedding.html")

def whoisuser2(request):
    return render(request,'whoisuser2.html')

#for graduation
def greduate(request):
    return render(request,'greduate.html')

def greduatedate(request):
    return render(request,'greduatedate.html')
    
def greduationgdata(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    address2 = request.POST.get('address2')
    city=request.POST.get('city')
    data=greduation()
    data.name=name
    data.email=email
    data.address=address
    data.address2=address2
    data.city=city
    data.save()
    return render(request,'greduate.html')


def ss(request):
    return render(request,'ss.html')


def logout(request):
    del request.session['username']
    return render(request,'index.html')'''
