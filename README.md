# Hospital Management System
## Django ke saath bana hua complete hospital software

---

## Kya kya features hain?

| Module       | Kya karta hai                                      |
|--------------|----------------------------------------------------|
| Patients     | Marz register karna, edit, delete, search          |
| Doctors      | Doctor add karna, speciality, fee, availability    |
| Appointments | Marz ko doctor se milana, status track karna       |
| Pharmacy     | Dawaiyan ka stock, price, expiry track karna       |
| Billing      | Bill banana, paid/unpaid track karna               |
| Wards/Beds   | Ward banana, bed assign karna, status dekhna       |

---

## Pehli baar chalane ka tarika

### Step 1 — Django install karein
```
pip install django pillow
```

### Step 2 — Folder mein jaayein
```
cd hospital_project
```

### Step 3 — Database banayein
```
python manage.py makemigrations
python manage.py migrate
```

### Step 4 — Admin user banayein
```
python manage.py createsuperuser
```
(Username, Email aur Password darj karein)

### Step 5 — Server chalayein
```
python manage.py runserver
```

### Step 6 — Browser mein kholein
```
http://127.0.0.1:8000
```

---

## Ya ek hi baar mein setup karein (Linux/Mac)
```
bash setup.sh
```

---

## Login kaise karein?
- URL: `http://127.0.0.1:8000/login/`
- Username: jo aapne createsuperuser mein diya
- Password: jo aapne createsuperuser mein diya

---

## Admin Panel
- URL: `http://127.0.0.1:8000/admin/`
- Yahan se seedha database mein data dekh sakte hain

---

## Folder Structure
```
hospital_project/
├── manage.py                  ← Server chalane ka file
├── setup.sh                   ← Auto setup script
├── hospital_project/
│   ├── settings.py            ← Project settings
│   └── urls.py                ← Main URLs
├── patients/                  ← Marz module
├── doctors/                   ← Doctors module
├── appointments/              ← Appointments module
├── pharmacy/                  ← Pharmacy module
├── billing/                   ← Billing module
├── wards/                     ← Wards/Beds module
└── templates/                 ← Sab HTML files
    ├── base.html              ← Main layout (sidebar)
    ├── login.html             ← Login page
    ├── dashboard.html         ← Home page
    ├── patients/
    ├── doctors/
    ├── appointments/
    ├── pharmacy/
    ├── billing/
    └── wards/
```

---

## Koi masla aaye toh?

1. `ModuleNotFoundError: No module named 'django'`
   → `pip install django` chalayein

2. `OperationalError: no such table`
   → `python manage.py migrate` chalayein

3. Login nahi ho raha
   → `python manage.py createsuperuser` se naya user banayein

---

Made with Django | Bootstrap 5
