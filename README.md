# Backend - Portfolio Contact API

This is the backend API for my personal portfolio contact form, built with FastAPI, SQLAlchemy, and FastAPI-Mail.

## Features

- Receives contact form submissions (name, email, message)
- Stores messages in a PostgreSQL database via SQLAlchemy ORM
- Sends email notifications using FastAPI-Mail and Gmail SMTP
- CORS enabled for frontend integration
- Environment variables used for credentials and config

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [FastAPI-Mail](https://github.com/sabuhish/fastapi-mail)
- [PostgreSQL](https://www.postgresql.org/)
- Python 3.9+

## Setup

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd backend
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a `.env` file**

```env
DATABASE_URL=postgresql://user:password@host:port/dbname
MY_MAIL_USERNAME=your_email@gmail.com
MY_MAIL_PASSWORD=your_gmail_app_password
MY_MAIL_FROM=your_email@gmail.com
MAIL_RECEIVER=your_email@gmail.com
```

5. **Run the server**

```bash
uvicorn app.main:app --reload
```

## API

### `POST /contact`

Saves contact data and sends an email notification.

**Request body example:**

```json
{
  "name": "Juan Pancho",
  "email": "juanelpancho@example.com",
  "message": "Hi Hector, I liked your portfolio. Let's talk!"
}
```

## License

This project is licensed under the [MIT License](./LICENSE).
