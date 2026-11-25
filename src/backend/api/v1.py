from fastapi import APIRouter


router = APIRouter()

@router.get("/vad-tycker-linus", response_model=str)
def get_hello_world() -> str:
    return "Hala är den finaste på planeten!"

