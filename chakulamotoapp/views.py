from django.shortcuts import render,redirect
from chakulamotoapp.models import Member

def index(request):
    return render(request, 'index.html')

def inner(request):
    return render(request, 'inner-page.html')

def register(request):
    if request.method == 'POST':
        members = Member(username=request.POST['username'],
                         email=request.POST['email']
                       , password=request.POST['password'])

        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')


def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'],
                                 password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'],
                                        password=request.POST['password'])
            return render(request, 'adminhome.html', {'member':member})
        else:
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')
