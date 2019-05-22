from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('/auth/login/')