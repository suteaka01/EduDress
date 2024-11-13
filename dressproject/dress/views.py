from django.views.generic import ListView, DetailView
from .models import Question
from django.shortcuts import render

def index_view(request):
    return render(request, "dress/index.html", {"user": request.user})

# 問題一覧表示
class ListQuestionsView(ListView):
    template_name = 'dress/quest_list.html'
    model = Question
    context_object_name = 'questions'

# 問題詳細表示
class QuestionDetailView(DetailView):
    template_name = 'dress/question_detail.html'
    model = Question
    context_object_name = 'question'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        selected_choice = request.POST.get('choice')
        correct = selected_choice == self.object.correct_answer
        return self.render_to_response(self.get_context_data(
            correct=correct,
            selected_choice=selected_choice
        ))

def home_view(request):
    return render(request, "dress/home.html", {"user": request.user})