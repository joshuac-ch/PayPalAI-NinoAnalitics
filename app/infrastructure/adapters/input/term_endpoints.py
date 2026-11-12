from fastapi import APIRouter,Depends
from app.infrastructure.adapters.input.schemas.Term import TermScheme
from app.infrastructure.adapters.dependencias import adapter_get_terms,adapter_save_terms

router=APIRouter()

@router.get("/g/{id}/")
async def get_terms(id:str,
                    adapter_get_terms=Depends(adapter_get_terms)):
    try:
        return await adapter_get_terms.get_terms(id)
    except Exception as e:
        return f"Ocurrio un erro en get_terms {e}"    


@router.post("/s/")
async def save_terms(terms:TermScheme,
                    adapter_save_terms=Depends(adapter_save_terms)):
    try:
        return await adapter_save_terms.save_terms(terms)
    except Exception as e:
        return f"Ocurrio un erro en save_terms {e}"    



