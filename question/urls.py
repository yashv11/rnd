from django.urls import path

from . import views
app_name = 'question'
urlpatterns = [
    
    path('question', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote', views.vote, name='vote'),
    # path('question/<int:question_id>/', views.indx, name='indx'),
    

]