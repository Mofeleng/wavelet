from fastapi import APIRouter, WebSocket, WebSocketDisconnect

twilio_websocket_router = APIRouter()

@twilio_websocket_router.websocket("/twilio")
async def twilio_stream(ws: WebSocket):
    await ws.accept()

    print("Accepted websocket")