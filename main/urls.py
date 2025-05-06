from django.urls import path
from . import views
from .views import QuestionListView, QuestionCreateView,QuestionUpdateView,QuestionDeleteView, QuestionListCreateView,QuestionRetrieveUpdateDestroyView

urlpatterns = [
    path('', views.home, name='home'),  
    path('quiz/', views.quiz_view, name='quiz'), 
    path('submitquiz/', views.submit_answer, name='submit_quiz'),   
    path('task/', views.tasks, name='task'), 
    path('questions/', QuestionListView.as_view(), name='question_list'), 
    path('questions/add/', QuestionCreateView.as_view(), name='question_create'),  
    path('<int:pk>/update/', QuestionUpdateView.as_view(), name='question_update'),
    path('<int:pk>/delete/', QuestionDeleteView.as_view(), name='question_delete'),
    path('api/qQuestionList', QuestionListCreateView.as_view(), name = 'QuestionListCreateAPI'),
    path('api/QuestionDestroy', QuestionRetrieveUpdateDestroyView.as_view(), name ='QuestionRetrieveUpdateDestroyAPIView'),
]
