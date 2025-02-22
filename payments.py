from bot import bot
import stripe
from aiogram import types

from config import STRIPE_SECRET_KEY, WEBHOOK_SECRET
from fastapi import FastAPI, Request

app = FastAPI()

stripe.api_key = STRIPE_SECRET_KEY

PRODUCT_PRICE_ID = "price_1QtzinDFVaHAgzueh4V9H6Oj"


async def buy_product(message: types.Message):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price": PRODUCT_PRICE_ID,
            "quantity": 1,
        }],
        mode="payment",
        success_url="https://yourwebsite.com/success",
        cancel_url="https://yourwebsite.com/cancel",
        metadata={"chat_id": str(message.chat.id)}
    )

    await message.answer(f"Pay at the link: {session.url}")


@app.post("/webhook")
async def stripe_webhook(request: Request) -> dict[str, str]:
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
    except Exception:
        return {"error": "Webhook error"}

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        chat_id = session["metadata"].get("chat_id")

        if chat_id:
            await bot.send_message(int(chat_id), "✅ Payment successful!")

    return {"status": "success"}