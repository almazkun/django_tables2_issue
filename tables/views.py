from django.views.generic import DeleteView
from django_tables2 import SingleTableView
from .models import Conversation
from .tables import ConversationTable
from django.urls import reverse_lazy
from django.shortcuts import redirect


# Create your views here.
class ConversationList(SingleTableView):
    template_name = "home.html"
    model = Conversation
    table_class = ConversationTable


class ConversationDelete(DeleteView):
    model = Conversation

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(reverse_lazy("home"))
