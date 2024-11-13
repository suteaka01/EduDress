from django.urls import path
from . import views
from .views import ListQuestionsView, QuestionDetailView

urlpatterns = [
    path('', views.index_view, name='index'),  # トップページ
    path('home/', views.home_view, name='home'),  # 追加: ホームページ
    path('questions/', ListQuestionsView.as_view(), name='question_list'),  # 問題一覧ページ
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),  # 問題詳細ページ
    
]
