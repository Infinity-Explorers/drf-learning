# 🚀 DRF Learning Journey

Welcome to the **Django REST Framework (DRF) Learning Journey** repository by **Infinity Explorers**! This repository tracks a hands-on learning series designed to take you from core Django API fundamentals to building scalable, production-grade REST APIs using DRF.

---

## 📌 Repository Structure & Branches

This repository is organized into dedicated branches for each meeting and session. Each branch represents a milestone with focused concepts, code examples, and practice apps:

| Branch | Meeting | Key Topics Covered |
| :--- | :--- | :--- |
| [`main`](https://github.com/Infinity-Explorers/drf-learning/tree/main) | **Overview** | Learning roadmap, documentation, and repository index |
| [`meetings/meeting-1`](https://github.com/Infinity-Explorers/drf-learning/tree/meetings/meeting-1) | **Meeting 1** | Intro to DRF, HTTP methods, and Django `JsonResponse` |
| [`meetings/meeting-2`](https://github.com/Infinity-Explorers/drf-learning/tree/meetings/meeting-2) | **Meeting 2** | Serializers, Deserialization, Validation, and `APIView` |
| [`meetings/meeting-3`](https://github.com/Infinity-Explorers/drf-learning/tree/meetings/meeting-3) | **Meeting 3** | Django ORM, QuerySets, Field Lookups, and `Q` Objects |
| [`meetings/meeting-4`](https://github.com/Infinity-Explorers/drf-learning/tree/meetings/meeting-4) | **Meeting 4** | Complete CRUD operations & DRF Generic Views |

---

## 📚 Curriculum Breakdown

### 🔹 Meeting 1: Introduction to DRF & HTTP Methods
- Understanding REST architecture and how APIs work.
- Standard HTTP methods: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`.
- Returning JSON responses directly with Django's built-in `JsonResponse`.
- Setting up URL routing for API endpoints.

```bash
git checkout meetings/meeting-1
```

---

### 🔹 Meeting 2: Serializers & Class-Based `APIView`
- What is Serialization? Converting complex model and dictionary data into native Python datatypes that can easily be rendered into JSON.
- Deserialization: Parsing incoming request payloads.
- Data validation using `serializer.is_valid()` and handling `serializer.errors`.
- Class-Based Views with `rest_framework.views.APIView`.
- Standardized HTTP status codes (`HTTP_200_OK`, `HTTP_201_CREATED`, `HTTP_400_BAD_REQUEST`, etc.).

```bash
git checkout meetings/meeting-2
```

---

### 🔹 Meeting 3: Django ORM & Complex Queries
- Working with Django Models and QuerySets.
- CRUD operations via ORM (`objects.all()`, `create()`, `get()`, `filter()`, `update()`).
- Advanced Field Lookups:
  - `price__gte` (greater than or equal)
  - `price__lte` (less than or equal)
  - `name__startswith`
- Combining filters and complex conditions using Django's `Q` object (`&`, `|`, `~`).
- Ordering QuerySets with `order_by()`.

```bash
git checkout meetings/meeting-3
```

---

### 🔹 Meeting 4: Full CRUD & Generic Views
- Building full CRUD endpoints using `APIView`:
  - `GET`: Retrieve list of records or a single record
  - `POST`: Create a new record
  - `PUT`: Complete update of an existing record
  - `PATCH`: Partial update of an existing record
  - `DELETE`: Remove a record
- Transitioning from manual `APIView` implementations to DRF **Generic Class-Based Views**:
  - `ListCreateAPIView`: Handles listing and creating records in minimal lines of code.
  - `RetrieveUpdateDestroyAPIView`: Handles retrieving, updating, and deleting individual records seamlessly.

```bash
git checkout meetings/meeting-4
```

---

## 🛠️ Getting Started

Follow these steps to run the code locally from any branch:

### 1. Clone the Repository
```bash
git clone https://github.com/Infinity-Explorers/drf-learning.git
cd drf-learning
```

### 2. Switch to the Desired Meeting Branch
```bash
git checkout meetings/meeting-4
# Or any other meeting branch (meeting-1, meeting-2, meeting-3)
```

### 3. Set Up a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install django djangorestframework
```

### 5. Apply Migrations & Run Development Server
```bash
# Navigate to the meeting folder containing manage.py
cd meeting-4

# Run database migrations
python manage.py migrate

# Start the local development server
python manage.py runserver
```

Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## 🤝 Contributing & Community

Maintained with ❤️ by the **Infinity Explorers** team. Feel free to open issues or submit pull requests for improvements and additions!
