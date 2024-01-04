from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django_tables2 import SingleTableView
from .models import Conversation
from .tables import ConversationTable


# Create your views here.
class ConversationList(SingleTableView):
    template_name = "home.html"
    model = Conversation
    table_class = ConversationTable


class ConversationDelete(DeleteView):
    model = Conversation
    success_url = "/"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)
