# Blog Project

## Overview

A simple **Blog Application** built with **Django**,**HTML**,**CSS**,**JS** and **Bootstrap**. Allows users to create, view, update, delete, and comment on blog posts.

## Features

- **User Authentication:** Login and logout.
- **Post Management:** Create, update, delete, and view posts.
- **Drafts:** Manage unpublished posts.
- **Comments:** Add, approve, and remove comments on posts.
- **Post Publishing:** Publish drafts.

## Technologies

- **Backend:** Django (Python 3.x)
- **Frontend:** HTML, CSS (Bootstrap)
- **Database:** SQLite (default)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blog-project.git
   cd blog-project
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
    source venv/bin/activate  # macOS/Linux
    # or
    venv\Scripts\activate  # Windows

3. Install dependencies:
   ```bash
     pip install -r requirements.txt

4. Apply database migrations:
   ```bash
     python manage.py migrate

5. Create a superuser for admin access:
     ```bash
     python manage.py createsuperuser

6. Run the development server:
   ```bash
     python manage.py runserver

   
