import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()


def get_zoom_token():
    account_id = os.getenv("ZOOM_ACCOUNT_ID")
    client_id = os.getenv("ZOOM_CLIENT_ID")
    client_secret = os.getenv("ZOOM_CLIENT_SECRET")

    credentials = f"{client_id}:{client_secret}"

    encoded = base64.b64encode(
        credentials.encode()
    ).decode()

    url = (
        "https://zoom.us/oauth/token"
        f"?grant_type=account_credentials"
        f"&account_id={account_id}"
    )

    response = requests.post(
        url,
        headers={
            "Authorization": f"Basic {encoded}"
        }
    )

    if response.status_code != 200:
        raise Exception(
            f"Zoom token error: {response.text}"
        )

    return response.json()["access_token"]