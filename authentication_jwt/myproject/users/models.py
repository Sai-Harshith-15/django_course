from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PATIENT = "PATIENT", "Patient"
        DOCTOR = "DOCTOR", "Doctor"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class PatientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.PATIENT)


class Patient(User):

    base_role = User.Role.PATIENT

    patient = PatientManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "only for patients"

# class PatientProfile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE)
#   patient_id = models.IntegerField(null=True, blank=True)


class DoctorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.DOCTOR)

class Doctor(User):

    base_role = User.Role.DOCTOR

    patient = DoctorManager()

    class Meta:
        proxy = True

    def welcome(self):
        return "only for doctors"
