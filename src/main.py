from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from clesiemo3 import __version__
from clesiemo3.router import api_router

app = FastAPI(
    title="My App",
    version=__version__,
    description="This is my project description",
    openapi_url="/api/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.include_router(api_router)


@app.get("/")
async def root():
    return RedirectResponse(url="/api/docs")
