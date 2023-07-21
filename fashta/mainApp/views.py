from django.shortcuts import render,HttpResponseRedirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.messages import success,error

def homePage(Request):
    products = product.objects.all().order_by("-id")[0:12]
    return render(Request,'index.html',{'products' : products})


def shopPage(Request,mc,sc,br):
    if(mc=="All" and sc=="All" and br=="All"):
        products = product.objects.all().order_by("-id")
    elif(mc!="All" and sc=="All" and br=="All"):
        products = product.objects.filter(maincategoryproduct = maincategory.objects.get(name=mc)).order_by("-id")
    elif(mc=="All" and sc!="All" and br=="All"):
        products = product.objects.filter(subcategoryproduct = subcategory.objects.get(name=sc)).order_by("-id")
    elif(mc=="All" and sc=="All" and br!="All"):
        products = product.objects.filter(brandproduct = brand.objects.get(name=br)).order_by("-id")
    elif(mc!="All" and sc!="All" and br=="All"):
        products = product.objects.filter(maincategoryproduct = maincategory.objects.get(name=mc), subcategoryproduct = subcategory.objects.get(name=sc)).order_by("-id")
    elif(mc=="All" and sc!="All" and br!="All"):
        products = product.objects.filter(subcategoryproduct = subcategory.objects.get(name=sc), brandproduct = brand.objects.get(name=br)).order_by("-id")
    elif(mc!="All" and sc=="All" and br!="All"):
        products = product.objects.filter(maincategoryproduct = maincategory.objects.get(name=mc), brandproduct = brand.objects.get(name=br)).order_by("-id")
    else:
        products = product.objects.filter(maincategoryproduct = maincategory.objects.get(name=mc), subcategoryproduct = subcategory.objects.get(name=sc), brandproduct = brand.objects.get(name=br)).order_by("-id")
    
    
    maincategorys = maincategory.objects.all().order_by("id")
    subcategorys = subcategory.objects.all().order_by("-id")
    brands = brand.objects.all().order_by("id")
    return render(Request,'shop.html',{'products': products, 'maincategorys': maincategorys, 'subcategorys' : subcategorys, 'brands' : brands, 'mc' : mc, 'sc' : sc, 'br' : br})


def shopDetailsPage(Request,id):
    products = product.objects.get(id=id)
    return render(Request,'shop-details.html',{'products':products})


def shoppingCartPage(Request):
    return render(Request,'shopping-cart.html')


def checkOutPage(Request):
    return render(Request,'checkout.html')


def aboutPage(Request):
    return render(Request,'about.html')


def contactPage(Request):
    return render(Request,'contact.html')


def loginPage(Request):
    if(Request.method=="POST"):
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username = username, password = password)
        if(user is not None):
            login(Request,user)
            if(user.is_superuser):
                return HttpResponseRedirect("/admin/")
            else:
                return HttpResponseRedirect("/profile/")
        else:
            error(Request,"Invalid Username or Password!!")
    return render(Request,'login.html')


def signupPage(Request):
    if(Request.method=="POST"):
        password = Request.POST.get("password")
        cpassword = Request.POST.get("cpassword")
        if(password == cpassword):
            name = Request.POST.get("name")
            username = Request.POST.get("username")
            email = Request.POST.get("email")
            phone = Request.POST.get("phone")

            try:
                User.objects.create_user(username = username, email = email, password = password, first_name = name)

                b = buyer()
                b.name = name
                b.email = email
                b.username = username
                b.phone = phone
                b.save()
                return HttpResponseRedirect("/login/")
            except:
                error(Request,"Username Already Taken!!!")
        else:
            error(Request,"Password and Confirm Password doesn't match!")
    return render(Request,'signup.html')


def logoutView(Request):
    logout(Request)
    return HttpResponseRedirect("/")

def profilePage(Request):
    if(Request.user.is_superuser):
        return HttpResponseRedirect("/admin/")
    username = Request.user.username
    try:
        buyerdata = buyer.objects.get(username = username)
        mywishlist = wishlist.objects.filter(buyer = buyerdata)
        return render(Request,"profile.html",{"buyerdata" : buyerdata,'wishlist' : mywishlist })
    except:
        return HttpResponseRedirect("/login/")
    

def updateprofilePage(Request):
    if(Request.user.is_superuser):
        return HttpResponseRedirect("/admin/")
    username = Request.user.username
    try:
        buyerdata = buyer.objects.get(username=username)
        if(Request.method=="POST"):
            buyerdata.name = Request.POST.get("name")
            buyerdata.email = Request.POST.get("email")
            buyerdata.phone = Request.POST.get("phone")
            buyerdata.city = Request.POST.get("city")
            buyerdata.state = Request.POST.get("state")
            buyerdata.pin = Request.POST.get("pin")
            buyerdata.address = Request.POST.get("address")
            if(Request.FILES.get("pic")):
                buyerdata.pic = Request.FILES.get("pic")
            buyerdata.save()
            return HttpResponseRedirect("/profile/")
        return render(Request,"update-profile.html",{"buyer": buyerdata})
    except:
        return HttpResponseRedirect("/login/")
    
def mywishlist(Request,id):
    try:
        buyerproduct = buyer.objects.get(username = Request.user.username)
        products = product.objects.get(id=id)
        try:
            w = wishlist.objects.get(product=products,buyer=buyerproduct)
        except:
            w = wishlist()
            w.product = products
            w.buyer = buyerproduct
            w.save()
    except:
        return HttpResponseRedirect("/login/")
    return HttpResponseRedirect("/profile/")

def deletewishlist(Request,id):
    products = wishlist.objects.get(id=id)
    products.delete()
    return HttpResponseRedirect("/profile/")