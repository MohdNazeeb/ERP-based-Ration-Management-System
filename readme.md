# 🌾 Smart Ration ERP – A Complete Ration Distribution Management System

Smart Ration ERP is a scalable and secure Django-based system designed to digitalize and streamline ration distribution for government and private sectors.  
It manages distributors, citizens, transactions, authentication, inventory tracking, announcements, eKYC, and automated allocation workflows — all in one unified platform.

---

## 🚀 Features

### 🔐 **Authentication & Role Management**
- Secure login for Distributors and Admins  
- Custom user model (Aadhaar integration, shop ID, user roles)

### 🧾 **Ration Distribution System**
- Allocate ration based on predefined quotas  
- Track issued ration, pending quotas, and distribution history  
- Citizen verification with Aadhaar number  

### 📊 **Dashboard & Insights**
- Visual dashboard for distributors  
- Daily & monthly ration statistics  

### 📝 **eKYC Verification Module**
- Aadhaar-based verification  
- Status tracking for individuals  

### 🔔 **Announcement System**
- Admin can push announcements  
- Distributors can access real-time updates  

### 📦 **Inventory & Stock Management**
- Stock in/out  
- Low-stock alerts  
- Shop-wise ration stock levels  

### 🗂️ **User-Friendly UI**
- Clean Django Templates  
- Responsive design (HTML, CSS, Bootstrap)

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| **Backend** | Django, Python |
| **Database** | SQLite (development), any SQL DB (production) |
| **Frontend** | HTML, CSS, JavaScript |
| **Server** | Django WSGI/ASGI |
| **Auth** | Django Auth + CustomUser |

---

## 📁 Folder Structure

```plaintext
Smart-Ration-ERP/
│
├── manage.py
├── db.sqlite3
│
├── core/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── distributor/
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   │     └── distributor/
│   │           └── (HTML template files)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── user/
│   ├── __pycache__/
│   ├── migrations/
│   ├── static/
│   │     └── user/
│   │           └── (CSS, JS, Images)
│   ├── templates/
│   │     └── user/
│   │           └── (HTML templates)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
└── media/
      └── (Uploaded files such as images, documents)

```

## 🧩 Module Overview

The Smart Ration ERP project is organized into multiple Django apps, each responsible for a specific part of the system. Below is a clear overview of all modules:

---

### 🔵 **`user` App**
This module manages all **user-side features**, including authentication and profile management.

#### **Responsible For:**
- User Login & Logout  
- User Registration  
- Serving static files (CSS/JS)  
- Rendering user-facing HTML templates  
- Handling user-related views and logic  

#### **Important Files:**
- `user/views.py` → User login, register, dashboard views  
- `user/models.py` → User model extensions (if any)  
- `user/templates/user/` → User HTML templates  
- `user/static/user/` → CSS, JS, icons

---

### 🟠 **`distributor` App**
This module handles everything related to ration distribution and distributors.

#### **Responsible For:**
- Distributor Login & Dashboard  
- Ration Distribution Workflow  
- Verifying Ration Cards / Families  
- Managing Ration Stock  
- Tracking Allocation History  
- Rendering distributor UI pages  

#### **Important Files:**
- `distributor/views.py` → Distribution logic, dashboard  
- `distributor/models.py` → Stock, Allocation, RationCard models  
- `distributor/templates/distributor/` → Distributor HTML pages  

---

### ⚫ **`core` App**
This is the central configuration app of your Django project.

#### **Responsible For:**
- Django project-level configuration  
- Registering installed apps  
- URL routing for all apps  
- WSGI & ASGI application files  

#### **Important Files:**
- `core/settings.py` → Project settings  
- `core/urls.py` → Global URL patterns  
- `core/wsgi.py` → Deployment entry point  
- `core/asgi.py` → Async server entry point  

---

### 🟣 **`media/` Directory**
Stores all uploaded files such as:
- Aadhaar images  
- Ration card documents  
- Proof images  

---

### 🟢 **Project Root**
Contains essential files:
- `manage.py` → Main command-line utility  
- `requirements.txt` → Python package list  

---

## 📸 Screenshots & UI Preview

![Login Screen](screenshots/login.png)
![Distributor Dashboard](screenshots/dashboard.png)
![Ration Allocation](screenshots/allocation.png)
