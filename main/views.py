from django.shortcuts import render, redirect
from .models import Task,Question,Choice
from .models import Questions
from .forms import QuestionForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy


# quiz_data = [
#     {"id": 1, "question": "What is the capital of Nepal?", "options": ["Pokhara", "Bakhtapur", "Kathmandu", "New Delhi"], "answer": "Kathmandu"},
#     {"id": 2, "question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
#     {"id": 3, "question": "What is the largest ocean on Earth?", "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"], "answer": "Pacific Ocean"},
#     {"id": 5, "question": "Which element has the chemical symbol 'O'?", "options": ["Oxygen", "Gold", "Silver", "Iron"], "answer": "Oxygen"}
# ]

def home(request):
    return render(request, "home.html", {"message": "Hello Django"})

def quiz_view(request):
    quiz_data = Questions.objects.all()
    return render(request, 'quiz.html', {'quiz_data': quiz_data})


def submit_answer(request):
    if request.method == 'POST':
        score = 0
        total = Questions.objects.count()

        for question in Questions.objects.all():
            selected = request.POST.get(f'q{question.id}') 
            
            if selected and selected == question.correct_answer:
                score += 1

        percentage = (score / total) * 100 if total > 0 else 0

        context = {
            'score': score,
            'total': total,
            'percentage': round(percentage, 2)
        }

        return render(request, 'quiz_result.html', context)

    return redirect('quiz_view')

def tasks(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        if 'add' in request.POST:
            desc = request.POST.get('task')
            if desc:
                Task.objects.create(description=desc)
        elif 'remove' in request.POST:
            task_id = request.POST.get('task_id')
            if task_id:
                Task.objects.filter(id=task_id).delete()
            else:
                Task.objects.all().delete()  
    return render(request, 'task.html', {'tasks': tasks})


class QuestionListView(ListView):
    """Display all quiz questions"""
    model = Questions
    template_name = 'question_list.html'
    paginate_by = 10
    ordering = ['-created_at']

class QuestionCreateView(CreateView):
    """Create new quiz question"""
    model = Questions
    form_class = QuestionForm
    template_name = 'question_form.html'
    success_url = reverse_lazy('question_list')

class QuestionUpdateView(UpdateView):
    model = Questions
    form_class = QuestionForm
    template_name = 'question_update.html'
    success_url = reverse_lazy('question_list')

class QuestionDeleteView(DeleteView):
    model = Questions
    template_name = 'question_delete.html'  
    success_url = reverse_lazy('question_list')


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import QuestionModelSerializer

class QuestionListCreateView(ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionModelSerializer

class QuestionRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionModelSerializer