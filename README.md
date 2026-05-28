# StartupHub — Startup Platform

A Django-based platform connecting startups, investors, and mentors.

## Features
- **Startup Owners**: Register startups, track ratings, connect with investors/mentors
- **Investors**: Browse and rate startups, connect with founders
- **Mentors**: View and mentor startups, give feedback
- **Connections**: Send/accept/reject connection requests
- **Real-time Chat**: Message connected users (polls every 3s)

## Setup & Run

```bash
# 1. Create virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Mac/Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Create admin user (optional)
python manage.py createsuperuser

# 5. Run server
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

## Test Accounts (already in db.sqlite3)
| Username       | Password | Role     |
|----------------|----------|----------|
| teststartup    | test123  | Startup  |
| testmentor     | test123  | Mentor   |
| testinvestor   | test123  | Investor |

## Project Structure
```
startup_platform/
├── core/               # Main app
│   ├── models.py       # User, Startup, Mentor, Investor, ConnectionRequest, ChatRoom, Message
│   ├── views.py        # All views
│   └── templates/      # HTML templates
├── static/             # CSS, JS, Images
├── startup_platform/   # Django settings & URLs
├── db.sqlite3          # SQLite database
└── manage.py
```
