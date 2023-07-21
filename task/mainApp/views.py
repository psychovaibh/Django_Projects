from django.shortcuts import render



def homePage(Request):
    return render(Request,'index.html')