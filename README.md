# News-App
# 📰 News With

A modern Flask-based News Web Application that fetches real-time headlines using the NewsAPI. Users can search for news, browse categories, register, log in, and save their favorite articles as bookmarks.

---

## 📸 Preview

<img width="100%" alt="News With App" src="https://via.placeholder.com/1000x500?text=News+With+App">

> Replace this image with a screenshot of your application after uploading it to GitHub.

---

## ✨ Features

- 🔍 Search news by keyword
- 🌍 Browse top headlines
- 📰 News Categories
  - Business
  - Technology
  - Sports
  - Health
  - Science
  - Entertainment
- 👤 User Registration
- 🔐 User Login & Logout
- ❤️ Bookmark Articles
- 🗑 Remove Bookmarks
- 📱 Responsive Bootstrap UI
- 🔑 Secure Password Hashing
- 💾 SQLite Database

---

## 🛠 Tech Stack

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite
- Bootstrap 5
- HTML5
- CSS3
- Jinja2
- NewsAPI
- Requests

---

## 📂 Project Structure

```text
News-With/
│
├── app.py
├── models.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── bookmarks.html
│
├── static/
│   └── css/
│       └── style.css
│
└── instance/
    └── news.db
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/sagargs999/News-App.git
```

Move into the project

```bash
cd flask-news-app
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux/Mac

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```env
NEWS_API_KEY=YOUR_NEWSAPI_KEY
```

Get your free API key from:

https://newsapi.org/

---

## ▶ Run the Project

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page

- Top Headlines
- Search News
- Categories

### Login

- Secure Authentication

### Register

- Create New Account

### Bookmarks

- Save Favorite Articles
- Remove Bookmarks

---

## 🚀 Future Improvements

- Dark Mode
- Pagination
- Trending News
- User Profile
- Email Verification
- Password Reset
- Bookmark Search
- News Recommendations
- Infinite Scroll
- Deployment on Render

---

## 👨‍💻 Author

**Sagar GS**

GitHub:
https://github.com/sagargs999

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is licensed under the MIT License.
