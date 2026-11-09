from app.domain.ports.term_port import TermPort

class GetTermUseCase:

    def __init__(self,term_port:TermPort):
        self.ter_port=term_port

    async def get_terms(self,term_id):
        try:
            return await self.ter_port.get(term_id)
        except Exception as e:
            print("Ocurrio un error en getTerm",e)         