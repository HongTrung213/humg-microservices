@echo off
cd /d D:\CODE\humg-microservices\notification-service
python manage.py send_warnings >> D:\CODE\humg-microservices\logs\send_warnings_%date:~-4,4%%date:~-7,2%%date:~-10,2%.log 2>&1