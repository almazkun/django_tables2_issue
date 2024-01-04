from django.urls import path
from tables.views import ConversationList, ConversationDelete

urlpatterns = [
    path("", ConversationList.as_view(), name="home"),
    path("delete/<int:pk>/", ConversationDelete.as_view(), name="conversation_delete"),
]
