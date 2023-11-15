from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView, DeleteView
from .models import Inbox
from django.db.models import OuterRef, Subquery, Q, Max

# Create your views here.


# class InboxTemplateView(TemplateView):
#     template_name = 'inbox/messages.html'

class InboxListView(ListView):
    model = Inbox
    template_name = 'inbox/messages.html'
    context_object_name = 'messages'

    # def get_queryset(self):
    #     # Subquery to get the most recent message for each conversation
    #     subquery_sender = Inbox.objects.filter(
    #         sender=OuterRef('sender')
    #     ).order_by('-date_created').values('body')[:1]

    #     subquery_receiver = Inbox.objects.filter(
    #         receiver=OuterRef('receiver')
    #     ).order_by('-date_created').values('body')[:1]

    #     # Query to get the most recent message from each conversation to the current user
    #     queryset = Inbox.objects.filter(
    #         Q(sender=self.request.user) | Q(receiver=self.request.user)
    #     ).annotate(
    #         most_recent_sender_message=Subquery(subquery_sender),
    #         most_recent_receiver_message=Subquery(subquery_receiver)
    #     )

    #     return queryset

    def get_queryset(self):
        # Subquery to get the date of the most recent message for each sender
        subquery = Inbox.objects.filter(sender=OuterRef('sender')).values('sender').annotate(
            max_date=Max('date_created')).values('max_date')[:1]

        # Query to get the most recent message from each sender to the current user
        queryset = Inbox.objects.filter(receiver=self.request.user).filter(
            date_created=Subquery(subquery)
        )

        return queryset


class InboxDetailView(DetailView):
    model = Inbox
    template_name = 'inbox/detail_message.html'
    context_object_name = 'message'
    pk_url_kwarg = 'inbox_pk'
