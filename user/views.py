from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    credit=100
    return render(request,'signin.html',{'credit':credit})