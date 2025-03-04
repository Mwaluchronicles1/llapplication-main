from django.contrib import admin
from .models import UserProgress, QuizAttempt


@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'completed',
                    'last_accessed', 'completion_date')
    list_filter = ('completed', 'last_accessed')
    search_fields = ('user__email', 'lesson__title')


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz', 'score', 'passed', 'completed_at')
    list_filter = ('passed', 'completed_at')
    search_fields = ('user__email', 'quiz__title')
