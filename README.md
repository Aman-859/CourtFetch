# CourtFetch - Delhi High Court Case Data Scraper

CourtFetch is a Django-based web application that allows users to search Delhi High Court case details using case type, number, and year. It uses Selenium to scrape the live data from the official website and displays it in a clean UI.

## 🚀 Features

- Simple web interface to input case details
- CAPTCHA auto-detection and solving (text-based)
- Selenium-based headless scraping using Chromium (Render compatible)
- Logging of every search query to SQLite
- Displays results in a Bootstrap-powered table
- Option to download attached PDFs if available

## 🏛️ Court Targeted

- **Delhi High Court**
- URL: https://delhihighcourt.nic.in/app/case-number

## 🧠 Strategy for CAPTCHA

- This website uses a simple text-based CAPTCHA that is directly visible on the page.
- We extract the CAPTCHA value using Selenium and fill it automatically (no image-based OCR required).

## 🛠️ Local Setup Instructions

```bash
git clone https://github.com/Aman-859/CourtFetch.git
cd CourtFetch
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then go to http://localhost:8000 and search for a case.

## 📁 Folder Structure

- `CourtFetch/` - Django project root
- `CourtFetchapp/` - Main application logic (views, models, utils)
- `templates/` - HTML frontend (Bootstrap UI)
- `db.sqlite3` - SQLite database
- `utils.py` - Contains the Selenium logic to fetch case data

## 📸 Demo Video

[Watch Demo Video](https://drive.google.com/file/d/1-demo-link-or-upload-here)

## 🧪 Environment Variables

Not required for this task. All values (like URL, captcha logic) are hardcoded.

## 📊 Sample Case Details to Test

| Case Type | Case Number | Filing Year |
|-----------|-------------|--------------|
| CW        | 8146        | 2023         |
| WP        | 1234        | 2022         |

