from django.shortcuts import render

# Create your views here.
def user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    credit=100
    return render(request,'signin.html',{'credit':credit})