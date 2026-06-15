<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2563EB,50:06B6D4,100:22C55E&height=180&section=header&text=ZipLink&fontSize=54&fontColor=ffffff&fontAlignY=38&desc=Fast%20and%20simple%20URL%20shortener&descSize=18&descAlignY=58" alt="ZipLink project banner" width="100%" />

# ZipLink

### A clean URL shortener built with Flask, SQLite, and Tailwind CSS

ZipLink helps users convert long URLs into short, easy-to-share links. It also tracks visits and lets users manage saved links from a simple dashboard.

<br>

<img src="https://skillicons.dev/icons?i=python,flask,sqlite,html,tailwind,git,github,vscode&theme=light" alt="Tech logos" />

<br>
<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-Frontend-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)

![Project Type](https://img.shields.io/badge/Project-Major_Project-16A34A?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-2563EB?style=for-the-badge)
![Made With](https://img.shields.io/badge/Made_With-Clean_Code-F97316?style=for-the-badge)

[![GitHub](https://img.shields.io/badge/GitHub-ggauravky-181717?style=flat-square&logo=github)](https://github.com/ggauravky)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-gauravky-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/gauravky/)
[![Portfolio](https://img.shields.io/badge/Portfolio-ggauravky.vercel.app-000000?style=flat-square&logo=vercel)](https://ggauravky.vercel.app/)

</div>

---

## Table of Contents

- [About ZipLink](#about-ziplink)
- [Why This Project](#why-this-project)
- [Core Features](#core-features)
- [Pages and Routes](#pages-and-routes)
- [Services and Modules](#services-and-modules)
- [Tech Stack](#tech-stack)
- [How ZipLink Works](#how-ziplink-works)
- [Database Design](#database-design)
- [Project Structure](#project-structure)
- [Setup and Run](#setup-and-run)
- [User Guide](#user-guide)
- [Current Limitations](#current-limitations)
- [Future Scope](#future-scope)
- [Learning Outcomes](#learning-outcomes)
- [Author](#author)

---

## About ZipLink

ZipLink is a full-stack URL shortener project. It takes a long website link and creates a shorter link that is easier to share.

In simple words:

- User enters a long URL.
- App creates a short code.
- Short code becomes a short URL.
- User can open the short URL.
- App redirects to the original URL.
- App counts every visit.
- User can delete saved links.

---

## Why This Project

This project is useful because long URLs are hard to share, remember, and manage. ZipLink solves that with a clean dashboard and simple backend logic.

This project shows:

- Flask routing
- Form handling
- SQLite database operations
- Jinja template rendering
- URL redirection
- Visit tracking
- Delete functionality
- Clean frontend UI with Tailwind CSS

---

## Core Features

| Feature | Simple Explanation |
| --- | --- |
| Short URL creation | Converts a long URL into a short code |
| URL redirection | Opens the original URL when the short link is clicked |
| Visit tracking | Counts how many times each short link is opened |
| Link dashboard | Shows all saved short links in one place |
| Delete link | Removes a short URL from the database |
| 404 page | Shows a clean error page for invalid short links |
| Local database | Stores all links in SQLite |
| Responsive UI | Works on desktop and smaller screens |

---

## Pages and Routes

### Home Page

Route: `/`

What it does:

- Shows the main ZipLink dashboard.
- Contains the URL input form.
- Lists all shortened URLs.
- Shows original URL, short URL, and visit count.
- Provides a delete button for each saved URL.

### Create Short URL

Route: `/`

Method: `POST`

What it does:

- Receives the URL from the form.
- Generates a random short code.
- Saves the original URL and short code in the database.
- Redirects back to the home page.

### Short URL Redirect Page

Route: `/<short_code>`

Method: `GET`

What it does:

- Finds the original URL using the short code.
- Increases the visit count.
- Redirects the user to the original URL.
- Shows the 404 page if the short code is not found.

### Delete URL

Route: `/delete/<short_code>`

Method: `POST`

What it does:

- Deletes the selected short URL from the database.
- Sends the user back to the home page.

### About Route

Route: `/about`

Method: `GET`

What it does:

- Returns a simple about message.

### 404 Page

Template: `templates/404.html`

What it does:

- Shows a user-friendly error screen.
- Helps users return to the main app.
- Appears when a short code does not exist.

---

## Services and Modules

### `app.py`

Main Flask application file.

Responsibilities:

- Starts the Flask app.
- Defines all routes.
- Handles form submissions.
- Generates short codes.
- Connects routes with database functions.
- Redirects users to original URLs.
- Renders HTML templates.

Main functions:

| Function | Work |
| --- | --- |
| `generate_short_code()` | Creates a random short code |
| `index()` | Handles home page and URL creation |
| `redirect_url()` | Redirects short URL to original URL |
| `delete_short_url()` | Deletes a saved short URL |
| `about()` | Returns about page text |

### `model.py`

Database service file.

Responsibilities:

- Creates the database table.
- Inserts new URLs.
- Reads saved URLs.
- Updates visit count.
- Deletes URLs.

Main functions:

| Function | Work |
| --- | --- |
| `init_db()` | Creates the `urls` table if it does not exist |
| `insert_url()` | Saves original URL and short code |
| `get_url()` | Gets original URL using short code |
| `increment_visit_count()` | Adds 1 to the visit count |
| `get_all_urls()` | Gets all saved URLs |
| `delete_url()` | Deletes one URL by short code |

### `templates/index.html`

Main frontend page.

Responsibilities:

- Shows project title.
- Shows input form.
- Displays saved short links.
- Displays visit counts.
- Provides delete buttons.
- Uses Tailwind CSS for styling.

### `templates/404.html`

Error page.

Responsibilities:

- Shows message for invalid links.
- Provides a link back to the home page.
- Keeps the UI clean and consistent.

---

## Tech Stack

### Backend

| Tech | Use |
| --- | --- |
| Python | Main programming language |
| Flask | Web framework and routing |
| Jinja2 | Template rendering through Flask |
| SQLite3 | Database support using Python standard library |
| Random module | Short code generation |
| String module | Characters used in short code generation |

### Frontend

| Tech | Use |
| --- | --- |
| HTML5 | Page structure |
| Tailwind CSS | Styling and responsive layout |
| Jinja syntax | Dynamic data display in HTML |
| Browser forms | URL input and delete actions |

### Tools

| Tool | Use |
| --- | --- |
| Git | Version control |
| GitHub | Source code hosting |
| VS Code | Development editor |
| Markdown | Project documentation |

---

## How ZipLink Works

### Shortening Flow

```text
User enters URL
      |
      v
Flask receives form data
      |
      v
App creates random short code
      |
      v
SQLite stores original URL and short code
      |
      v
Home page shows the new short URL
```

### Redirect Flow

```text
User clicks short URL
      |
      v
Flask reads short code from route
      |
      v
SQLite finds original URL
      |
      v
Visit count increases
      |
      v
User is redirected to original website
```

### Delete Flow

```text
User clicks Delete
      |
      v
Flask receives delete request
      |
      v
SQLite removes the matching short code
      |
      v
Home page refreshes
```

---

## Database Design

Database file:

```text
database.db
```

Table name:

```text
urls
```

### Table Columns

| Column | Type | Purpose |
| --- | --- | --- |
| `id` | INTEGER | Unique ID for every record |
| `original_url` | TEXT | The full destination URL |
| `short_code` | TEXT | The generated short code |
| `visit_count` | INTEGER | Number of times the short link was opened |

### Database Query Work

- Insert a new URL.
- Find URL by short code.
- Increase visit count.
- Get all URLs.
- Delete URL by short code.

---

## Project Structure

```text
ZipLink/
+-- app.py
+-- model.py
+-- database.db
+-- README.md
+-- templates/
|   +-- index.html
|   +-- 404.html
+-- .gitignore
```

### File Details

| File | Purpose |
| --- | --- |
| `app.py` | Main Flask app and route handling |
| `model.py` | SQLite database functions |
| `database.db` | Local SQLite database file |
| `templates/index.html` | Main dashboard UI |
| `templates/404.html` | Not found page |
| `.gitignore` | Files ignored by Git |
| `README.md` | Project documentation |

---

## Setup and Run

### 1. Clone the Project

```bash
git clone https://github.com/ggauravky/ZipLink.git
cd ZipLink
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

macOS or Linux:

```bash
source .venv/bin/activate
```

### 4. Install Flask

```bash
pip install flask
```

### 5. Run the App

```bash
python app.py
```

### 6. Open in Browser

```text
http://127.0.0.1:5000
```

---

## User Guide

### Create a Short Link

- Open the home page.
- Paste a full URL.
- Click `Shorten URL`.
- Copy or open the generated short URL.

### Open a Short Link

- Click the short URL from the table.
- The app redirects to the original website.
- The visit count increases automatically.

### Delete a Link

- Click `Delete` for a saved URL.
- Confirm the delete action.
- The link is removed from the dashboard.

### Invalid Link

- If the short code does not exist, the app shows the 404 page.
- User can return to the home page.

---

## Current Limitations

- Short codes are generated randomly.
- Custom short codes are not available yet.
- No user login system yet.
- All users share the same local database.
- No expiry date for links yet.
- No copy button yet.

---

## Future Scope

- Add copy-to-clipboard button.
- Add custom short URL option.
- Add user login and personal dashboards.
- Add link expiry date.
- Add search and filter.
- Add analytics charts.
- Add QR code generation.
- Add deployment support.
- Add REST API endpoints.

---

## Learning Outcomes

This project helps understand:

- How Flask routes work.
- How HTML forms send data.
- How SQLite stores records.
- How backend and frontend connect.
- How URL redirection works.
- How visit tracking can be implemented.
- How clean project documentation is written.

---

## Author

<div align="center">

### Gaurav Kumar Yadav

Full-stack developer focused on building useful, clean, and practical web projects.

[![GitHub](https://img.shields.io/badge/GitHub-ggauravky-181717?style=for-the-badge&logo=github)](https://github.com/ggauravky)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-gauravky-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/gauravky/)
[![Portfolio](https://img.shields.io/badge/Portfolio-ggauravky.vercel.app-000000?style=for-the-badge&logo=vercel)](https://ggauravky.vercel.app/)

</div>

---

<div align="center">

### Built with Python, Flask, SQLite, and Tailwind CSS

If this project helps you, consider giving it a star on GitHub.

</div>
