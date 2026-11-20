from fastapi import FastAPI
from .routes import twilio_websocket_router, twilio_webhook_router

app = FastAPI()
app.include_router(twilio_webhook_router, prefix="/api/v1/webhook", tags=["Twilio webhooks"])
app.include_router(twilio_websocket_router, prefix="/api/v1/ws/stream", tags=["Twilio audio stream"])
