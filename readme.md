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


