from fastapi import APIRouter, Request
from app.api.controllers.test_api_controller import TestApiController
test_router = APIRouter(
    prefix='/chat'
)

@test_router.post('/question')
async def question(req: Request):
    question = await req.json()
    return TestApiController().get_response_for_question(question)