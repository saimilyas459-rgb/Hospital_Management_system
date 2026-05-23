#!/bin/bash
echo "======================================"
echo "  Hospital Management System Setup"
echo "======================================"

# Install Django
echo ""
echo "Step 1: Django install ho raha hai..."
pip install django pillow

# Migrations
echo ""
echo "Step 2: Database tables ban rahe hain..."
python manage.py makemigrations patients
python manage.py makemigrations doctors
python manage.py makemigrations appointments
python manage.py makemigrations pharmacy
python manage.py makemigrations billing
python manage.py makemigrations wards
python manage.py migrate

# Create superuser
echo ""
echo "Step 3: Admin user banana hai"
echo "Neeche apna username, email aur password darj karein:"
python manage.py createsuperuser

echo ""
echo "======================================"
echo "  Setup Mukammal!"
echo "  Ab yeh command chalayein:"
echo "  python manage.py runserver"
echo "  Phir browser mein kholein:"
echo "  http://127.0.0.1:8000"
echo "======================================"
