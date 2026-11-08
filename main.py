from app.infrastructure.adapters.input.users_endpoints import router as router_users

from app.infrastructure.adapters.input.product_endpoints import router as router_products

from app.infrastructure.adapters.input.term_endpoints import router as router_terms

from app.infrastructure.adapters.input.order_endpoints import router as router_orders

from app.infrastructure.adapters.output.connection import CreateConection
from fastapi import FastAPI,APIRouter,Request
from contextlib import asynccontextmanager

# Conexion Mongo
connection=CreateConection()
@asynccontextmanager
async def lifespan(app:FastAPI):
    await connection.connect()

    app.state.connection= connection

    yield

    await connection.close()

app=FastAPI(lifespan=lifespan)
router=APIRouter()
router.include_router(router_users,prefix="/users",tags=["Users"])
router.include_router(router_products,prefix="/products",tags=["Products"])
router.include_router(router_terms,prefix="/terms",tags=["Terms"])
router.include_router(router_orders,prefix="/orders",tags=["Orders"])
app.include_router(router)



@app.get("/")
async def main():
    try:
        print("App corriendo")
        return "Corriendo app"
    except Exception as e:
        print("Ocurrio un error",e)    
