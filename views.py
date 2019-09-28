from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from kwik.models import test




def testing(request):
    if request.method == 'POST':
        print(request.POST)
        uname = request.POST.getlist('name[]', '')
        umail = request.POST.getlist('mail[]', '')
        uphone = request.POST.getlist('phone[]', '')
        print(len(uname))
        i = 0
        while i < len(uname):
            names = uname[i]
            print(names)
            mails = umail[i]
            mobiles = uphone[i]

            # # this is checking the variable, if variable is null so fill the varable value in database
            if names != "" and mails != "" and mobiles != "":
                test.objects.create(name=names, mail=mails, mobile=mobiles)

            i = i + 1

        return HttpResponse('Your Record Has been Saved')

    else:
        return render(request, 'test.html')
