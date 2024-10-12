from django.db import models
from django.conf import settings
import uuid

class Client(models.Model):
    id = models.UUIDField(primary_key=True)  # Don't use default=uuid.uuid4
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.company_name


class ServiceProvider(models.Model):
    id = models.UUIDField(primary_key=True)  # Don't use default=uuid.uuid4
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    service_offered = models.CharField(max_length=255)

    def __str__(self):
        return self.business_name


class Experience(models.Model):
    id = models.UUIDField(primary_key=True)  # Don't use default=uuid.uuid4
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.job_title


class Skill(models.Model):
    id = models.UUIDField(primary_key=True)  # Don't use default=uuid.uuid4
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    proficiency_level = models.CharField(max_length=50, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])

    def __str__(self):
        return self.skill_name