<div align="center">

<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />

# ⚡ Evalify

### *Where Startups Meet Capital & Mentorship*

A full-stack Django web platform that bridges the gap between **startup founders**, **investors**, and **mentors** — featuring smart rating systems, real-time chat, and connection management.

[🚀 Live Demo](#) • [📖 Docs](#project-structure) • [🐛 Report Bug](https://github.com/Tanishq-tawar/Evalify/issues) • [✨ Request Feature](https://github.com/Tanishq-tawar/Evalify/issues)

</div>

---

## 📸 Screenshots

> **Home Page**

<!-- Add screenshot here -->
<!-- ![Home Page](screenshots/home.png) -->
<img width="1919" height="1063" alt="Screenshot 2026-05-28 232942" src="https://github.com/user-attachments/assets/cc0485b3-ef0e-49f1-beaf-82cc5a7fb035" />

> **Startup **

<!-- Add screenshot here -->
<!-- ![Startup Dashboard](screenshots/startup_dashboard.png) -->
<img width="1884" height="1048" alt="Screenshot 2026-05-29 004426" src="https://github.com/user-attachments/assets/071393fc-6c0d-4da1-b67f-f7c003b3884b" />


---

> **Mentors**

<!-- Add screenshot here -->
<!-- ![Mentor Dashboard](screenshots/mentor_dashboard.png) -->
<img width="1895" height="1048" alt="Screenshot 2026-05-29 004416" src="https://github.com/user-attachments/assets/9d248c15-c6bc-409f-9524-65f1f4a933d6" />


---

> **Mentor Dashboard**

<!-- Add screenshot here -->
<!-- ![Investor Dashboard](screenshots/investor_dashboard.png) -->
<img width="1901" height="1052" alt="Screenshot 2026-05-29 004446" src="https://github.com/user-attachments/assets/f617825a-65b3-4922-9b7b-8b29f4cb234a" />


---

> **Login Page**

<!-- Add screenshot here -->
<!-- ![Mentors Page](screenshots/mentors.png) -->
<img width="1919" height="1063" alt="Screenshot 2026-05-28 233103" src="https://github.com/user-attachments/assets/a6364d67-6f5d-49c4-81f6-b7dc7c860782" />


---

> **About Us**

<!-- Add screenshot here -->
<!-- ![Chat](screenshots/chat.png) -->
<img width="1899" height="1061" alt="Screenshot 2026-05-28 233022" src="https://github.com/user-attachments/assets/61dc04a6-3a71-49b8-a4e0-13cfd60816f9" />


---

## 🌟 Features

### For Startup Owners
- ✅ Register and manage multiple startups
- ✅ Upload startup logos and profile details
- ✅ Get auto-calculated ratings based on market potential, scalability, and traction
- ✅ Connect with investors and mentors
- ✅ View and respond to mentor feedback

### For Investors
- ✅ Browse all startups ranked by rating
- ✅ Filter startups by industry and name
- ✅ View detailed startup profiles with metrics
- ✅ Connect directly with founders via email or in-app chat
- ✅ Upload and display a profile photo

### For Mentors
- ✅ Discover startups ready for mentoring
- ✅ Leave structured feedback and evaluations
- ✅ Upload a profile photo shown on the public Mentors page
- ✅ Connect and chat with startup founders

### Platform-Wide
- ✅ **Smart Rating Engine** — auto-computes a 0–10 startup score from three dimensions
- ✅ **Connection System** — send, accept, and reject connection requests
- ✅ **Real-time Chat** — polling-based messaging (every 3 seconds) between connected users
- ✅ **Role-based Dashboards** — separate dashboards for startups, investors, and mentors
- ✅ **Media Uploads** — logos and profile photos stored and served dynamically
- ✅ **Responsive Design** — works on desktop and mobile

---

## 🏗️ Project Structure

```
Evalify/
│
├── core/                          # Main Django app
│   ├── migrations/                # Database migrations
│   ├── templates/                 # All HTML templates
│   │   ├── Home.html              # Landing page
│   │   ├── startupdash.html       # Startup owner dashboard
│   │   ├── mentordash.html        # Mentor dashboard
│   │   ├── investordash.html      # Investor dashboard
│   │   ├── Mentors.html           # Public mentors listing
│   │   ├── Startups.html          # Public startups listing
│   │   ├── startup_profile.html   # Individual startup page
│   │   ├── add_startup.html       # Add startup form
│   │   ├── edit_startup.html      # Edit startup form
│   │   ├── connections.html       # Connection requests
│   │   ├── chat_room.html         # Real-time chat
│   │   ├── inbox.html             # Chat inbox
│   │   ├── login.html             # Login page
│   │   ├── Signup.html            # Registration page
│   │   └── Aboutus.html           # About page
│   ├── models.py                  # Database models
│   ├── views.py                   # View logic
│   ├── admin.py                   # Django admin config
│   └── apps.py
│
├── startup_platform/              # Django project config
│   ├── settings.py                # Project settings
│   ├── urls.py                    # URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── static/                        # Static assets
│   ├── css/                       # Stylesheets per page
│   ├── js/                        # JavaScript files
│   └── image/                     # Static images
│
├── media/                         # User-uploaded files
│   ├── startup_logos/             # Startup logo uploads
│   ├── mentor_photos/             # Mentor profile photos
│   └── investor_photos/           # Investor profile photos
│
├── db.sqlite3                     # SQLite database
├── manage.py                      # Django CLI
└── requirements.txt               # Python dependencies
```

---

## 🧠 Data Models

| Model | Key Fields |
|---|---|
| `User` | `username`, `email`, `role` (startup / investor / mentor / admin), `bio`, `profile_pic` |
| `Startup` | `name`, `description`, `industry`, `logo`, `market_potential`, `scalability`, `traction`, `rating` |
| `Mentor` | `user`, `expertise`, `experience`, `rating`, `bio`, `photo` |
| `Investor` | `user`, `investment_range`, `focus_areas`, `bio`, `photo` |
| `ConnectionRequest` | `sender`, `receiver`, `status` (pending / accepted / rejected) |
| `ChatRoom` | `participants` (M2M), `created_at` |
| `Message` | `room`, `sender`, `content`, `timestamp`, `is_read` |

### ⭐ Rating Algorithm

A startup's overall score is automatically computed on every save:

```
Rating = ( Market Potential + Scalability + Traction ) / 3
```

Each dimension is scored 0–10 via a questionnaire when adding or editing a startup.

---

## ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 4.x (Python) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Database | SQLite (dev) |
| Auth | Django built-in auth with custom `User` model |
| File Storage | Django `ImageField` + local `MEDIA_ROOT` |
| Realtime | Polling (JS `setInterval` every 3s) |
| Fonts | Google Fonts (Poppins) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Tanishq-tawar/Evalify.git
cd Evalify

# 2. Create and activate a virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. (Optional) Create a superuser for admin panel
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.

> The admin panel is available at **http://127.0.0.1:8000/admin/**

---

## 🔑 Test Accounts

The `db.sqlite3` file already includes seed data. Use these accounts to explore the platform immediately:

| Username | Password | Role |
|---|---|---|
| `teststartup` | `test123` | Startup Owner |
| `testmentor` | `test123` | Mentor |
| `testinvestor` | `test123` | Investor |

---

## 🗺️ URL Routes

| URL | View | Description |
|---|---|---|
| `/` | `home` | Landing page |
| `/signup/` | `signup_view` | User registration |
| `/login/` | `login_view` | User login |
| `/dashboard/` | `dashboard` | Role-based dashboard |
| `/mentors/` | `mentors` | Public mentor listing |
| `/startups/` | `startups` | Public startup listing |
| `/add-startup/` | `add_startup` | Add new startup |
| `/startup/<id>/` | `startup_profile` | Startup detail page |
| `/startup/edit/<id>/` | `edit_startup` | Edit startup |
| `/connect/<user_id>/` | `send_connection_request` | Send connection request |
| `/connections/` | `connections` | Manage connections |
| `/inbox/` | `inbox` | Chat inbox |
| `/chat/<room_id>/` | `chat_room` | Chat room |
| `/update-mentor-photo/` | `update_mentor_photo` | Upload mentor photo |
| `/update-investor-photo/` | `update_investor_photo` | Upload investor photo |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📋 Roadmap

- [ ] Email notifications for connection requests
- [ ] OAuth login (Google / GitHub)
- [ ] WebSocket-based real-time chat (Django Channels)
- [ ] Advanced startup search and filtering
- [ ] Investor portfolio tracking dashboard
- [ ] Public API endpoints
- [ ] Deployment guide (Railway / Render / PythonAnywhere)

---

## 🪪 License

This project is open source. Feel free to use and modify it.

---

<div align="center">

Made with ❤️ by [Tanishq Tawar](https://github.com/Tanishq-tawar)

⭐ Star this repo if you found it helpful!

</div>
