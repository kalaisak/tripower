from django.shortcuts import render

def home(request):
    return render(request,'main.html')


def home1(request):
    mobile=request.GET ["mobile"]
    return render(request,'main1.html',{'mobile':mobile})


def home2(request):
    return render(request,'main2.html')
