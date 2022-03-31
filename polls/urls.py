from django.urls import path

from django.views.generic.base import TemplateView
from . import views

app_name ='polls'
urlpatterns = [
    # /polls/
    path('', views.create_questions, name='createQ'),

    # /polls/tags/
    path('tags/', views.get_list_all_tags, name='getalltag'),

    #page4.html
    path('page4/', views.page4, name='page4'),

    path('page3/<id>/', views.page3, name='page3'),

    #/polls/<id>/
    path('<id>/', views.update_vote, name='put_update'),

path('graph/<id>/',views.graph,name='graph'),
    # /polls/detail/
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    # /polls/detail/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),


    # /polls/detail/votes/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
