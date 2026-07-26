from django.db import models


class Student(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    qualification = models.CharField(max_length=100)

    skills = models.TextField()

    password = models.CharField(max_length=100)

    resume = models.FileField(
        upload_to='resumes/',
        null=True,
        blank=True
    )


    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    job_type = models.CharField(max_length=50)
    description = models.TextField()
    last_date = models.DateField()

    def __str__(self):
        return self.title


class Application(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
    )


    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )


    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )


    applied_date = models.DateField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.student.name} - {self.job.title}"