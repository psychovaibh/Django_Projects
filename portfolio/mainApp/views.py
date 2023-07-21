from django.shortcuts import render

# Create your views here.
def homePage(Request):
    return render(Request,'index.html')