from django.contrib import admin
from .models import Course, Question, Result, CheatingAttempt

# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)

@admin.register(CheatingAttempt)
class CheatingAttemptAdmin(admin.ModelAdmin):
    list_display = ['student', 'exam', 'violation_type', 'timestamp']
    list_filter = ['violation_type', 'timestamp', 'exam']
    search_fields = ['student__user__username', 'student__user__first_name', 'exam__course_name']
    readonly_fields = ['timestamp']
