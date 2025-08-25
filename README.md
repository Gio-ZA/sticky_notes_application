# Sticky Notes Application 📝

A Django web application that allows users to create, view, edit, and delete sticky notes.  
Built with Django, SQLite, and Bootstrap for a responsive and user-friendly interface.

---

## Features
- ➕ Create sticky notes with a title and content
- 📋 View a list of all notes
- ✏️ Edit existing notes
- ❌ Delete notes with confirmation
- 🎨 Styled with Bootstrap and custom CSS
- ⚙️ Organized templates, static files, and migrations

---

## Project Structure
sticky_notes/
│── notes/ # Main app
│ ├── migrations/ # Database migrations
│ ├── static/ # CSS & other static files
│ ├── templates/ # HTML templates
│ ├── tests.py # Unit tests
│ ├── views.py # App logic
│ ├── models.py # Database models
│ ├── urls.py # App URLs
│── sticky_notes/ # Project config (settings, urls, wsgi, asgi)
│── manage.py

---

## Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/Gio-ZA/sticky-notes.git
   cd sticky-notes

2. Create and activate a virtual environment:
   python -m venv myenv
   source myenv/bin/activate   # Mac/Linux
   myenv\Scripts\activate      # Windows

3. Install dependencies:
   pip install -r requirements.txt


4. Run migrations:
   python manage.py migrate

5. Start the development server:
   python manage.py runserver

6. Open in your browser:
   http://127.0.0.1:8000/


Run all tests with:
python manage.py test

---

## License

This project is licensed under the MIT License.
