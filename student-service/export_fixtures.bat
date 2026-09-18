@echo off
chcp 65001 >nul
cd /d D:\CODE\humg-microservices\student-service
set DEBUG=True
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
echo Dang export fixtures...
python manage.py dumpdata students.Khoa --indent 2 --output students\fixtures\khoa.json
python manage.py dumpdata students.NganhDaoTao --indent 2 --output students\fixtures\nganh.json
echo.
echo Da xuat xong fixtures.
pause >nul
