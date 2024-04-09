Django User Referral System API

This repository contains a Django project that implements a user referral system API using Django REST Framework (DRF).

Features:
User authentication and registration.
User profile details retrieval.
Referral system with referrer and referred user tracking.
API endpoints for user registration, user details, and referrals.

Installation
1.Clone the repository:
git clone [https://github.com/your-username/django-user-referral-api.git](https://github.com/vaisagh-mp/Referral.git)

2.Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows

3.Install dependencies:
pip install -r requirements.txt

4.Apply migrations:
 python manage.py migrate
 
5.Create a superuser (admin):
python manage.py createsuperuser

6.Run the development server:
python manage.py runserver


API Endpoints:
POST /api/register/: Register a new user.
GET /api/user/details/: Retrieve user details.
GET /api/user/referrals/: List user's referrals.
