from app.domain.ports.conversation_port import ConversationPort

class ConversationCreateUseCase:

    def __init__(self,conversation_port:ConversationPort):
        self.conversation_port=conversation_port

    async def create_conversation(self,conversation):
        try:
            return await self.conversation_port.create(conversation)
        except Exception as e:
            return f"Error en save_conversation {e}"

    async def send_message_conversation(self,conversation_id,message):
        try:
            return await self.conversation_port.add_message(conversation_id,message)
        except Exception as e:
            return f"Error en send_message_conversation {e}"            