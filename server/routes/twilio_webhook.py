from fastapi import APIRouter, Response
from utils import get_env

twilio_webhook_router = APIRouter()

@twilio_webhook_router.post("/twilio")
def handle_incoming_call():
    WEBSOCKET_URL = get_env("TWILIO_WEBSOCKET_URL")

    response = (
        f"<?xml version='1.0' encoding='utf-8'>"
        f"<Response>"
            f"<Say>This call may be monitored or recorded</Say>"
            f"<Connect />"
                f"<Stream url='{WEBSOCKET_URL}' />"
            f"<Conntect />"
        f"</ Response>"
    )

    return Response(content=response, media_type="application/xml")
