from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Form
# Create your views here.

def main(request):
    return render(request, 'index.html')

def message(request):
    if request.method == 'POST':
        send = Form()
        send.name = request.POST.get('name')
        send.email = request.POST.get('email')
        send.address = request.POST.get('address')
        send.messages = request.POST.get('messages')
        send.save()
        return HttpResponseRedirect('/')
