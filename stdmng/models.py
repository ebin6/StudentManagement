from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=50,unique=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)

class Trainer(models.Model):
    name=models.CharField(max_length=60)
    employee_id = models.CharField(max_length=20,unique=True)
    phone = models.CharField(max_length=15)
    expertise = models.CharField(max_length=200)
    experience_years = models.PositiveSmallIntegerField(
        default=0,
        validators=[MaxValueValidator(60)],
    )
    qualification = models.CharField(max_length=150, blank=True)
    joined_at = models.DateField()

class Student(models.Model):
    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        OTHER = "other", "Other"
        NOT_SPECIFIED = "not_specified", "Prefer not to say"

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        GRADUATED = "graduated", "Graduated"


    admission_number = models.CharField(
        max_length=20,
        unique=True,
    )
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=15,
        choices=Gender.choices,
        default=Gender.NOT_SPECIFIED,
    )
    address = models.TextField()
    city = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    joined_at = models.DateField()
    # install pillow
    photo = models.ImageField(
        upload_to="students/photos/",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)