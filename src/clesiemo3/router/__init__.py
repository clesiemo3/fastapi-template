from fastapi import APIRouter

from .llm import router as llm_router

api_router = APIRouter(prefix="/api")
api_router.include_router(llm_router)
