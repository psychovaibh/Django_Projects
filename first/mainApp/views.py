from django.shortcuts import render

# Create your views here.

def homePage(Request):
    lv = 0
    lc = 0
    uv = 0
    uc = 0
    d = 0
    s = 0
    sp = 0
    show = False

    if(Request.method == "POST"):
        show = True
        message = Request.POST.get("message")

        for i in message:
            if(i>='a' and i<='z'):
                if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
                    lv += 1
                else:
                    lc += 1
            elif(i>='A' and i<='Z'):
                if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                    uv += 1
                else:
                    uc += 1
            elif(i>='0' and i<='9'):
                d = d + 1
            elif(i==" "):
                s += 1
            else:
                sp += 1
    return render(Request,"index.html", {'lv':lv, 'lc':lc, 'uv':uv, 'uc':uc, 'd':d, 's':s, 'sp':sp, 'show':show})


def aboutPage(Request):
    return render(Request,"about.html")


def contactPage(Request):
    return render(Request,"contact.html",
                  {
                      "name":"Vaibhav",
                      "phone":"8569991533",
                      "email":"vibuvaibhav1@gmail.com"
                  })


def galleryPage(Request):
    return render(Request,"gallery.html")


def profilePage(Request):
    data = [
        {"id":1002,"name":"Deepak Singh Gusain","dsg":"Trainer","salary":65000,"city":"Ghaziabad","state":"UP"},
        {"id":1003,"name":"Satyam Dixit","dsg":"Trainer","salary":50500,"city":"Noida","state":"UP"},
        {"id":1004,"name":"Mamta Jain","dsg":"Trainer","salary":75000,"city":"South Delhi","state":"Delhi"},
        {"id":1005,"name":"Rahul Sharma","dsg":"Manager","salary":120500,"city":"Noida","state":"UP"}
    ]
    return render(Request,"profile.html",{'datatable': data})