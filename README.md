# 🚀 Telegram Payment Bot

This is a Telegram bot that allows users to purchase products using Stripe payments. The bot sends a payment link and notifies the user upon successful payment.

---

## 📌 Features
- 💳 **Stripe Payments** – Secure transactions through Stripe.
- 🔗 **Checkout Links** – Users receive a payment link.
- ✅ **Payment Confirmation** – Users get notified when payment is completed.
- ⚡ **Webhook Integration** – Real-time updates on payments.

---

## 📌 Technologies Used
- `Python 3`
- `aiogram` – Telegram bot framework
- `FastAPI` – Webhooks handling
- `Stripe` – Payment processing
- `asyncio` – Asynchronous operations
- `uvicorn` – ASGI server

---

## 🔧 Installation Guide

### 📌 1. Clone the Repository
```bash
git clone https://github.com/FixbroYT/Telegram-payments-bot.git
cd Telegram-payments-bot
```

### 📌 2. Create a Virtual Environment
```bash
python -m venv .venv
```
Activate the virtual environment:
- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```bash
  source .venv/bin/activate
  ```

### 📌 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 📌 4. Configure Environment Variables
Create a `.env` file and add:
```env
BOT_TOKEN=your_telegram_bot_token
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
WEBHOOK_SECRET=your_stripe_webhook_secret
```
### 📌 5. Configure PRODUCT_PRICE_ID


### 📌 6. Run the Bot
```bash
python bot.py
```

### 📌 7. Start FastAPI Webhook Server
```bash
uvicorn payments:app --host 0.0.0.0 --port 8000
```

### 📌 8. Set Up Ngrok for Webhooks
If running locally, use Ngrok to expose the webhook:
```bash
ngrok http 8000
```
Copy the `https://` URL and set it as your webhook in Stripe Dashboard.

---

## 📌 API Endpoints
| Endpoint          | Method | Description                        |
|------------------|--------|----------------------------------|
| `/webhook`       | POST   | Stripe Webhook for payments     |

---

## 📌 Troubleshooting
- **Bot doesn’t start?** Ensure `.env` is set up correctly.
- **Webhook not working?** Check if Ngrok is running and URL is updated in Stripe.
- **Stripe error?** Verify the `STRIPE_SECRET_KEY` and `PRODUCT_PRICE_ID`.

---

## 📌 Contact
For any issues, reach out to **@Bobik6k** on Telegram.

🎉 **Your bot is ready to accept payments!**
