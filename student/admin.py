from django.contrib import admin
from student.models import UserProfile, Attendance, SubjectWiseAttendance, Result

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('enrol',)

admin.site.register(UserProfile, UserAdmin)
admin.site.register(Attendance)
admin.site.register(SubjectWiseAttendance)
admin.site.register(Result)