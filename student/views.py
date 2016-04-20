from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from student.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
import datetime
import json
from django.core import serializers
from django.contrib.auth import logout

# Create your views here.
from student.models import Attendance, Result, SubjectWiseAttendance


def index(request):
    return render(request, 'student/index.html')


def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

        else:
            print (user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} ;
    return render(request,'student/register.html', context)

@csrf_exempt
def user_login(request):

     if request.method == 'POST':

        enrol = request.POST.get('enrol')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        print (username)
        user = authenticate(username = username, email=email, password=password, enrol =enrol)

        if user:

            if user.is_active:

                login(request, user)
                attendance_data = SubjectWiseAttendance.objects.filter(enrol=enrol)
                attendance_datum = serializers.serialize("json",attendance_data)

                marks_data = Result.objects.filter(enrol = enrol)
                marks_datum = serializers.serialize("json", marks_data)
                contextStudent = {
                    'enrol': enrol,
                    'marks': marks_datum,
                    'attendance': attendance_datum  }

                return render(request, 'student/student.html', contextStudent)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            print ("Invalid login details: {0}, {1}".format(email, password, enrol))
            return HttpResponse("Invalid login details supplied.")


     else:
        return render(request, 'student/login.html', { })

@csrf_exempt
def attendance(request):

    if request.method == 'POST':

        if request.POST.get('present')== 'on':
            print("Here")
            enrol = request.POST.get('enrol')
            present = request.POST.get('present')

            if present=='on':
                status = True
            else:
                status = False

            a = Attendance(enrol= enrol, present=status, add_date = datetime.datetime.now() )
            a.save()


            return render(request, 'student/confirm.html', {'update':True, 'enrol':enrol})

        else:
            return render(request, 'student/student.html', {'update':False})


@login_required
def user_logout(request):

    logout(request)

    return HttpResponseRedirect('/student/')
