from app.domain.ports.term_port import TermPort

class SaveTermUseCase:

    def __init__(self,term_port:TermPort):
        self.term_port=term_port

    async def save_terms(self,terms):
            try:
                return await self.term_port.save(terms)
            except Exception as e:
                print("Ocurrio un error en saveTerm",e)     