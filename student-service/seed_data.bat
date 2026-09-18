@echo off
chcp 65001 >nul
cd /d D:\CODE\humg-microservices\student-service
set DEBUG=True
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
python manage.py seed_khoa_nganh_humg
echo.
echo Hoan tat. Nhan phim bat ky de thoat...
pause >nul
