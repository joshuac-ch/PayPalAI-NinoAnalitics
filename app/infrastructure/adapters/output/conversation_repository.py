from app.domain.ports.conversation_port import ConversationPort

class ConversationRepository(ConversationPort):

    def __init__(self):
        super().__init__()


    async def get_by_dispute(self, conversation_id):
        return await super().get_by_dispute(conversation_id)

    async def add_message(self, message):
        return await super().add_message(message)
        