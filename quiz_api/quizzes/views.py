from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from .models import Quiz, Question, Choice
from .serializers import (
    QuizSerializer, QuizDetailSerializer,
    QuestionSerializer, QuestionDetailSerializer,
    ChoiceSerializer, AnswerSerializer
)

@api_view(['GET'])
def api_root(request, format=None):
    base = request.build_absolute_uri('choices/')
    return Response({
        'quizzes': base + 'quizzes/',
        'questions': base + 'questions/',
        'choices': base + 'choices/',
    })

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuizDetailSerializer
        return QuizSerializer
    @action(detail=True, methods=['post'])
    def validate(self, request, pk=None):
        quiz = self.get_object()
        serializer = AnswerSerializer(data=request.data.get('answers', []), many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        answers = serializer.validated_data
        results = []
        for answer in answers:
            question_id = answer['question_id']
            choice_id = answer['choice_id']
            try:
                question = Question.objects.get(id=question_id, quiz=quiz)
                choice = Choice.objects.get(id=choice_id, question=question)
                results.append({
                    'question_id': question_id,
                    'correct': choice.is_correct,
                    'correct_choice': Choice.objects.filter(
                        question=question, is_correct=True
                    ).first().id if not choice.is_correct else None
                })
            except (Question.DoesNotExist, Choice.DoesNotExist):
                results.append({
                    'question_id': question_id,
                    'error': 'Question or choice not found'
                })
        correct_answers = sum(1 for r in results if r.get('correct', False))
        total_answers = len(results)
        return Response({
            'quiz_id': quiz.id,
            'score': f"{correct_answers}/{total_answers}",
            'percentage': int((correct_answers / total_answers) * 100) if total_answers else 0,
            'results': results
        })

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return QuestionDetailSerializer
        return QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
