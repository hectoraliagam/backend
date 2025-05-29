# Backend - Portfolio Contact API

This is the backend API for my personal portfolio contact form, built with FastAPI, SQLAlchemy, and FastAPI-Mail. It handles contact submissions, email notifications, and stores data securely.

## Features

- Receive contact form submissions with name, email, and message
- Store messages in a PostgreSQL database using SQLAlchemy ORM
- Send email notifications via FastAPI-Mail with Gmail SMTP
- Protect endpoints with reCAPTCHA v3 verification
- Rate limiting to prevent abuse (3 submissions per minute)
- CORS configured for seamless frontend integration
- Environment variables for all sensitive credentials and configuration

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [FastAPI-Mail](https://github.com/sabuhish/fastapi-mail)
- [PostgreSQL](https://www.postgresql.org/)
- Python 3.9+
- [httpx](https://www.python-httpx.org/) (for async HTTP requests)
- [slowapi](https://github.com/laurentS/slowapi) (rate limiting)
- [python-dotenv](https://github.com/theskumar/python-dotenv) (load .env variables)

## Setup and Run

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd backend
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
# On Linux/macOS
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file with your configuration**

```env
DATABASE_URL=postgresql://user:password@host:port/dbname
MY_MAIL_USERNAME=your_email@gmail.com
MY_MAIL_PASSWORD=your_gmail_app_password
MY_MAIL_FROM=your_email@gmail.com
MAIL_RECEIVER=receiver_email@example.com
RECAPTCHA_SECRET_KEY=your_recaptcha_secret_key
FRONTEND_URLS=https://yourfrontenddomain.com
```

5. **Run the development server**

```bash
uvicorn app.main:app --reload
```

## API Endpoint

### `POST /contact`

Accepts contact form submissions, verifies reCAPTCHA, stores data, and sends email notifications.

**Request body example:**

```json
{
  "name": "Juan Pancho",
  "email": "juanelpancho@example.com",
  "message": "Hi Hector, I liked your portfolio. Let's talk!"
}
```

**Headers:**

- `recaptcha-token`: the reCAPTCHA v3 token obtained from the frontend

**Rate Limit:** 3 requests per minute per IP

**Response:**

```json
{
  "message": "Thank you for contacting me, I will respond to you immediately."
}
```

## Notes

- Ensure your Gmail account has an App Password set if using 2FA.
- Adjust `FRONTEND_URLS` in your `.env` for CORS to allow requests from your frontend domain(s).
- reCAPTCHA v3 helps protect your backend from spam and abuse.

## License

This project is licensed under the [MIT License](./LICENSE).
