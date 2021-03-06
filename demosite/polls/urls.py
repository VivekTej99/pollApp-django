from django.urls import path
from . import views

appname = "polls"
urlpatterns = [
    path('', views.main, name="poll_main"),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]