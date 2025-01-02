from django.http import Http404
from django.shortcuts import render
from polling.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PollListView(ListView):
    model = Poll
    template_name = 'polling/list.html'


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polling/detail.html'

    def post(self, request, *args, **kwargs):
        poll = self.get_object()
        #.get_object() looks for id number of the poll that the request is for
        #retrieve indicated poll and make available in code
        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {"object": poll}
        return render(request, "polling/detail.html", context)