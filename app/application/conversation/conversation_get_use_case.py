from app.domain.ports.conversation_port import ConversationPort

class ConversationGetUseCase:

    def __init__(self,conversation_port:ConversationPort):
        self.conversation_port=conversation_port

    async def get_conversation(self,dispute_id):
        try:
            return await self.conversation_port.get_by_dispute(dispute_id)
        except Exception as e:
            return f"Ocurrio un error en get_conversation {e}"        