# DOMINIO
from app.domain.ports.user_port import UserPort


# CASOS DE USO
from app.application.users.GetUsers_use_case import GetUsersUseCase


from app.infrastructure.adapters.output.connection import CreateConection
from app.infrastructure.adapters.output.user_repository import UserRepository
# ADAPTADORES
connection_mongo=CreateConection()

user_adapter=UserRepository(connection_mongo)

adapter_get_user=GetUsersUseCase(user_port=user_adapter)
