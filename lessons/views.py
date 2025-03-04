from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Language, Lesson, PronunciationExercise
from .serializers import LanguageSerializer, LessonSerializer, PronunciationExerciseSerializer
from accounts.permissions import IsModerator
import speech_recognition as sr


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    # permission_classes = [IsModerator]


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    # permission_classes = [IsModerator]

    @action(detail=True, methods=['post'])
    def check_pronunciation(self, request, pk=None):
        lesson = self.get_object()
        audio_file = request.FILES.get('audio')

        if not audio_file:
            return Response(
                {'error': 'No audio file provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio)
            return Response({'transcribed_text': text})
        except sr.UnknownValueError:
            return Response(
                {'error': 'Could not understand audio'},
                status=status.HTTP_400_BAD_REQUEST
            )
