# Blog API

A modular, scalable backend API built with **FastAPI**, designed for managing users and blog posts. This project includes secure authentication, user management, and full CRUD operations for blogs.

---

## Features

* **User Management** – Register, retrieve, update, and delete users
* **Blog Post Management** – Create, view, update, and delete blog entries
* **Authentication** – JWT-based login and token handling using OAuth2
* **Built with** FastAPI, SQLAlchemy, Pydantic v2, and modern Python tooling

---

##  Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/)
* [Pydantic v2](https://docs.pydantic.dev/latest/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Passlib](https://passlib.readthedocs.io/en/stable/)
* [bcrypt](https://pypi.org/project/bcrypt/)
* [python-jose](https://python-jose.readthedocs.io/)
* [OAuth2PasswordBearer](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)

> **Note:** This project uses **Pydantic v2**. If you're coming from v1, syntax and config behavior have changed.

---

##  Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/JoseAyobami/llpp.git
cd llpp
```

### 2. Set up a virtual environment

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

Once running, access the API docs at:

* **Interactive Docs**: [http://localhost:8000/docs]


