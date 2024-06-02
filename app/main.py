from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers.text_api_router import test_router
app = FastAPI()

#corst
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get('/')
def root():
    return 'hola mundo'

#routers
app.include_router(test_router)