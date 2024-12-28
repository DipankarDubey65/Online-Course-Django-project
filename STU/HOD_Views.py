from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from app.models import Course,Session_Year,CustomUser,Student
from django.contrib.auth.models import User
from django.contrib import messages

@login_required(login_url='/')
def Home(request):
    return render(request,"Hod/home.html")

@login_required(login_url='/')
def Add_Student(request):

    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        print(profile_pic,first_name,last_name,email,username,password,address,gender,course_id,session_year_id)

        # Check email

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email are Already Exists !')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'username are Already Exists ! ')
            return redirect('add_student')
        else:
            user =CustomUser(
                profile_pic =profile_pic,
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            course = Course.objects.get(id = course_id)
            session_year = Session_Year.objects.get(id = session_year_id)

            student = Student(
                admin = user,
                address = address,
                session_year_id = session_year,
                course_id = course,
                gender = gender,

            )
            student.save()
            messages.success(request,'Student Successfully Saved')
            return redirect('add_student')


    context ={
        'course':course,
        'session_year':session_year,

    }

    return render(request,"Hod/add_student.html",context)


