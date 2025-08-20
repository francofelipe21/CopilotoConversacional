from pydantic import BaseModel
from fastapi import APIRouter
from backend.controllers.messages import new_msg
from agent.__init__ import agent, ctx

router = APIRouter()

class userMsg(BaseModel):
    msg: str

@router.post("/new_user_message")
async def new_user_msg(msg : userMsg):
    response = await new_msg(msg)
    return response