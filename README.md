<div align="center">

# ZipLink

**A clean and simple URL shortener built with Flask, SQLite, and Tailwind CSS.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

[![GitHub](https://img.shields.io/badge/GitHub-ggauravky-181717?style=flat-square&logo=github)](https://github.com/ggauravky)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-gauravky-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/gauravky/)
[![Portfolio](https://img.shields.io/badge/Portfolio-ggauravky.vercel.app-111827?style=flat-square&logo=vercel)](https://ggauravky.vercel.app/)

</div>

## About

ZipLink is a small web app that turns long URLs into short links. You paste a full URL, the app creates a short code, and you can use that short URL to redirect back to the original page.

It also tracks how many times each short link is visited and lets you delete links when you do not need them anymore.

## Features

- Create short URLs from long destination links.
- Open a short URL and redirect to the original website.
- Count visits for every short link.
- View all saved links in one table.
- Delete any saved short URL.
- Show a clean 404 page when a short code does not exist.
- Store data locally with SQLite.

## Tech Stack

| Technology | Use |
| --- | --- |
| Python | Main programming language |
| Flask | Backend web framework |
| SQLite | Local database |
| HTML | Page structure |
| Tailwind CSS | Frontend styling |

## How It Works

1. Enter a long URL in the input box.
2. ZipLink creates a random 6-character short code.
3. The original URL, short code, and visit count are saved in SQLite.
4. When someone opens the short URL, Flask finds the original URL.
5. The visit count increases by 1.
6. The user is redirected to the original website.

## Project Structure

```text
ZipLink/
+-- app.py
+-- model.py
+-- database.db
+-- templates/
|   +-- index.html
|   +-- 404.html
+-- README.md
```

## Routes

| Route | Method | Description |
| --- | --- | --- |
| `/` | GET | Shows the home page and all shortened URLs |
| `/` | POST | Creates a new short URL |
| `/<short_code>` | GET | Redirects to the original URL |
| `/delete/<short_code>` | POST | Deletes a saved short URL |
| `/about` | GET | Shows a basic about message |

## Setup

Clone the project:

```bash
git clone https://github.com/ggauravky/ZipLink.git
cd ZipLink
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install Flask:

```bash
pip install flask
```

Run the app:

```bash
python app.py
```

Open in your browser:

```text
http://127.0.0.1:5000
```

## Database

ZipLink uses SQLite. The database stores:

- Original URL
- Short code
- Visit count

The app creates the `urls` table automatically when it starts.

## Author

**Gaurav Kumar**

- GitHub: [@ggauravky](https://github.com/ggauravky)
- LinkedIn: [gauravky](https://www.linkedin.com/in/gauravky/)
- Portfolio: [ggauravky.vercel.app](https://ggauravky.vercel.app/)

## Future Improvements

- Add a copy button for short URLs.
- Allow custom short codes.
- Add user login.
- Add link expiry dates.
- Add search and filter options.

---

<div align="center">
Made with Python and Flask by <a href="https://github.com/ggauravky">Gaurav Kumar Yadav</a>
</div>
