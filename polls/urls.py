from nturl2path import url2pathname
from django.urls import path
from .views import vote, IndexView, ResultsView, DetailView

app_name="polls"

urlpatterns = [
    # ex: /polls/
    path("", IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path('<int:pk>/', DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", vote, name="vote"),
]
