**Vehicle Parking App**

A full-stack web app for managing vehicle parking lots. Admins create and manage parking lots and spots and view analytics. Users register, book a free spot in a lot, release it when leaving (cost is calculated automatically) and view their own parking history and spending charts. Background jobs send daily reminders and a monthly spending report by email.

**2. Features**

Admin

Create, edit and delete parking lots (spots Spot-1 … Spot-N are auto-generated)
View all lots with live available/occupied spots
Click a spot to see who occupies it, the vehicle number and the estimated cost
Search lots (by name/address/pin code) and look up users and their reservations
Summary charts: spot availability per lot and revenue per lot

User

Register / login
Browse lots, book an available spot with a vehicle number
Release a spot – parking duration and cost are computed (hours × lot price)
Dashboard with recent reservations, edit profile, spending/booking summary charts

Automated jobs (Celery Beat)

Daily at 18:06 – reminder email to users who have not booked that day
1st of every month at 01:00 – monthly spending report email


Prerequisites:

Python 3.9+
Node.js 16+ and npm
Redis running on localhost:6379 (cache + Celery)
A local SMTP catcher on port 1025 (e.g. MailHog or python -m aiosmtpd -n -l localhost:1025) – only needed for the email jobs

Setup & Run
Backend
bash
cd backend
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate

# No requirements.txt is included – install the packages the code imports:
pip install flask flask-sqlalchemy flask-security-too flask-restful flask-cors \
            flask-caching flask-mail celery redis passlib "sqlalchemy<2.1" email-validator

python app.py                       # API on http://localhost:5000

The database instance/db.sqlite3 is already included with the admin and user roles and two accounts, so no migration step is required.

Frontend
bash
cd frontend
npm install
npm run serve                       # http://localhost:8080 (proxies /api -> :5000)
Background jobs (optional, in separate terminals, from backend/)
bash
redis-server
celery -A celery_worker.celery worker --loglevel=info
celery -A celery_worker.celery beat   --loglevel=info


