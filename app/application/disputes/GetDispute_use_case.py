from app.domain.ports.dispute_port import DisputePort


class GetDisputeUseCase:

    def __init__(self,dispute_port:DisputePort):
        self.dispute_port=dispute_port


