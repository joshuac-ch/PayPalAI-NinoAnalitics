from app.domain.ports.LLM_port import LLMPort

class LLMRepository(LLMPort):

    def __init__(self):
        super().__init__()

    async def vision(self, prompt, image, schema):
        return await super().vision(prompt, image, schema)

    async def strutured(self, propmt, schema):
        return await super().strutured(propmt, schema)
        