from django.contrib import admin
from .models import Language, Lesson, PronunciationExercise


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    search_fields = ('name', 'code')
    list_filter = ('is_active',)


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'difficulty_level',
                    'order', 'created_at')
    list_filter = ('language', 'difficulty_level')
    search_fields = ('title', 'content')
    ordering = ('language', 'order')


@admin.register(PronunciationExercise)
class PronunciationExerciseAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'word')
    search_fields = ('word', 'lesson__title')
