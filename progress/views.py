from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProgress, QuizAttempt
from .serializers import UserProgressSerializer, QuizAttemptSerializer


class UserProgressViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user progress records.
    """
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer

    def get_queryset(self):
        """Filter queryset to return only the current user's progress"""
        return UserProgress.objects.filter(user=self.request.user)


class QuizAttemptViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing quiz attempts.
    """
    queryset = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer

    def get_queryset(self):
        """Filter queryset to return only the current user's quiz attempts"""
        return QuizAttempt.objects.filter(user=self.request.user)
