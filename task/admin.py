from django.contrib import admin
from task.models import FileType, Jobs, Applicants, Documents, JobsCategory
# Register your models here.

admin.site.register(Jobs)
admin.site.register(Applicants)
admin.site.register(Documents)
admin.site.register(FileType)
admin.site.register(JobsCategory)
