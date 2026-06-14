import requests
from auth import get_zoom_token


def create_zoom_meeting(
    topic: str,
    start_time: str,
    duration: int,
    user_email: str | None = None
):
    token = get_zoom_token()

    payload = {
        "topic": topic,
        "type": 2,
        "start_time": start_time,
        "duration": duration,
        "timezone": "Asia/Kolkata"
    }

    user_path = user_email or "me"
    response = requests.post(
        f"https://api.zoom.us/v2/users/{user_path}/meetings",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    if response.status_code not in [200, 201]:
        raise Exception(
            f"Zoom meeting error: {response.text}"
        )

    return response.json()