
from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import Student, Job, Application
from django.contrib import messages

def home(request):

    latest_jobs = Job.objects.all().order_by('-id')[:3]

    return render(
        request,
        'portal/home.html',
        {
            'latest_jobs': latest_jobs
        }
    )


def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        print("EMAIL:", email)
        print("PASSWORD:", password)

        try:
            student = Student.objects.get(email=email, password=password)

            request.session['student_id'] = student.id

            print("LOGIN SUCCESS")

            return redirect('dashboard')

        except Student.DoesNotExist:
            print("LOGIN FAILED")
            return render(request, 'portal/login.html',
                          {'error': 'Invalid Email or Password'})

    return render(request, 'portal/login.html')


def logout_view(request):
    request.session.flush()
    return redirect('home')


def register_view(request):

    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = StudentRegistrationForm()

    return render(request, 'portal/register.html', {'form': form})

def dashboard(request):

    if 'student_id' not in request.session:
        return redirect('login')

    student = Student.objects.get(id=request.session['student_id'])

    return render(request,
                  'portal/dashboard.html',
                  {'student': student})

def job_list(request):

    if 'student_id' not in request.session:
        return redirect('login')


    jobs = Job.objects.all()


    search = request.GET.get('search')
    location = request.GET.get('location')


    if search:
        jobs = jobs.filter(
            title__icontains=search
        ) | jobs.filter(
            company__icontains=search
        )


    if location:
        jobs = jobs.filter(
            location__icontains=location
        )


    return render(
        request,
        'portal/jobs.html',
        {
            'jobs': jobs
        }
    )
def apply_job(request, job_id):

    if 'student_id' not in request.session:
        return redirect('login')

    student = Student.objects.get(id=request.session['student_id'])

    job = Job.objects.get(id=job_id)

    application, created = Application.objects.get_or_create(
        student=student,
        job=job
    )

    if created:
        messages.success(request, "Application submitted successfully! 🎉")
    else:
        messages.info(request, "You already applied for this job.")

    return redirect('jobs')

def my_applications(request):

    if 'student_id' not in request.session:
        return redirect('login')

    student = Student.objects.get(id=request.session['student_id'])

    applications = Application.objects.filter(student=student)

    return render(request,
                  'portal/my_applications.html',
                  {'applications': applications})

def profile(request):

    if 'student_id' not in request.session:
        return redirect('login')

    student = Student.objects.get(
        id=request.session['student_id']
    )

    return render(
        request,
        'portal/profile.html',
        {'student': student}
    )

def upload_resume(request):

    if 'student_id' not in request.session:
        return redirect('login')


    student = Student.objects.get(
        id=request.session['student_id']
    )


    if request.method == "POST":

        student.resume = request.FILES['resume']
        student.save()

        return redirect('dashboard')


    return render(
        request,
        'portal/upload_resume.html',
        {'student': student}
    )
def admin_dashboard(request):

    total_students = Student.objects.count()

    total_jobs = Job.objects.count()

    total_applications = Application.objects.count()

    shortlisted = Application.objects.filter(
        status="Shortlisted"
    ).count()


    return render(
        request,
        'portal/admin_dashboard.html',
        {
            'total_students': total_students,
            'total_jobs': total_jobs,
            'total_applications': total_applications,
            'shortlisted': shortlisted,
        }
    )