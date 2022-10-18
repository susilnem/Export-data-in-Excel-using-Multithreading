from django.db import models
from django.contrib.auth.models import User
# Create your models here.\


JOB_TYPE = (("Fulll time", "Full time"), ("Part time",
            "Part time"), ("Internship", "Internship"))
CATEGORY = (("Citizenship", "Citizenship"),
            ("passport", "passport"), ("cv", "cv"))



class JobsCategory(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Jobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    location = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.ForeignKey(JobsCategory, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    salary = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


class FileType(models.Model):
    type = models.FileField(upload_to="documents")

    def __str__(self):
        return self.type.name


class Documents(models.Model):
    category = models.CharField(max_length=255, choices=CATEGORY, null=False)
    file = models.ManyToManyField(
        FileType, related_name="files")

    def __str__(self):
        return self.category


class Applicants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(
        Jobs, on_delete=models.CASCADE, related_name="jobs")
    documents = models.ManyToManyField(Documents, related_name="documents")

    def __str__(self):
        return self.user.username
