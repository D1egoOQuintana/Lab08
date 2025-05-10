from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizViewSet, QuestionViewSet, ChoiceViewSet, api_root

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('quizzes/', include(router.urls)),
    path('questions/', include(router.urls)),
    path('choices/', include(router.urls)),
]
