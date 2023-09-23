from rest_framework import serializers

from apps.conversation.models import Conversation, Message
from apps.core.serializers import DynamicFieldsModelSerializer


class InitiateConversationSerializer(serializers.Serializer):
    content = serializers.CharField()


class MessageSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = [
            "conversation",
            "translated_content",
            "translator",
            "sender",
        ]


class ConversationSerializer(DynamicFieldsModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = "__all__"
