from rest_framework import serializers
from .models import Language, Lesson, PronunciationExercise


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class PronunciationExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PronunciationExercise
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    pronunciation_exercises = PronunciationExerciseSerializer(
        many=True, read_only=True)
    language_name = serializers.CharField(
        source='language.name', read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'
