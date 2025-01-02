from django.urls import path
from polling.views import PollListView, PollDetailView

urlpatterns = [
    path('', PollListView.as_view(), name="poll_index"),
    #.as_view() is what actually shows up in class
    path('polls/<int:pk>/', PollDetailView.as_view(), name="poll_detail"),
]