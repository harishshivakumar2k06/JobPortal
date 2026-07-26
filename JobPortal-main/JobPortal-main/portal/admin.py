from django.contrib import admin
from .models import Student, Job, Application



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'qualification',
    )



@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'company',
        'location',
        'job_type',
        'last_date',
    )

    search_fields = (
        'title',
        'company',
    )





@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'job',
        'status',
        'applied_date',
    )


    list_filter = (
        'status',
    )