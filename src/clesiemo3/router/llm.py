from fastapi import APIRouter

router = APIRouter(prefix="/llm", tags=["llm"])


@router.get("/")
async def list_llms():
    return ["OpenAI", "Ollama"]
