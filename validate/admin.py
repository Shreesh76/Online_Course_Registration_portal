from django.contrib import admin
from .models import Profile, Department, teachers, Courses

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(teachers)
class teachersAdmin(admin.ModelAdmin):
    pass

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    pass
