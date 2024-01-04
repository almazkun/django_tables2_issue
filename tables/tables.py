import django_tables2 as tables
from .models import Conversation

class ConversationTable(tables.Table):
    delete = tables.TemplateColumn(
        template_name="conversation_delete.html", verbose_name="", orderable=False)
    
    class Meta:
        model = Conversation
        fields = ("name", "description", "date")