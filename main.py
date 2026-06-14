from fastapi import FastAPI
from pydantic import BaseModel

from zoom_client import create_zoom_meeting

app = FastAPI()


class MeetingRequest(BaseModel):
    topic: str
    start_time: str
    duration: int
    user_email: str


@app.post("/create-meeting")
def create_meeting(req: MeetingRequest):

    meeting = create_zoom_meeting(
        req.topic,
        req.start_time,
        req.duration,
        req.user_email
    )

    return {
        "meeting_id": meeting["id"],
        "join_url": meeting["join_url"],
        "start_url": meeting["start_url"],
        "password": meeting.get("password")
    }


@app.get("/callback")
def callback(code: str):
    return {
        "success": True,
        "code": code
    }