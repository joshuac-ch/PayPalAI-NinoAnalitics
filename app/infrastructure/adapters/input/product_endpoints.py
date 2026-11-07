from fastapi import APIRouter,Depends

from app.infrastructure.adapters.dependencias import (adapter_get_product,adapter_save_product)
from app.infrastructure.adapters.input.schemas.Producto import ProductoSchema
router=APIRouter()

@router.get("/g/{id}/")
async def get_product_by_id(id:str,
                            adapter_get_product=Depends(adapter_get_product)):
    try:
        return await adapter_get_product.get_product(id)

    except Exception as e:
        return f"Ocurrio un error {e}"    


@router.post("/p/")
async def save_product(product:ProductoSchema,
                       adapter_save_product=Depends(adapter_save_product)):
    try:
        return await adapter_save_product.create_product(product)
    except Exception as e:
        return f"Ocurrio un error {e}" 

@router.get("/all/")
async def get_list_product(adapter_get_product=Depends(adapter_get_product)):
    try:
        return await adapter_get_product.list_product()
    except Exception as e:
        return f"Ocurrio un error {e}"    
       
