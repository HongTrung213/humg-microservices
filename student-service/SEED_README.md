# Seed Data HUMG

## Du lieu
- 10 Khoa (ma 100-108, 401)
- 54 Nganh (48 dai tra + 6 chuong trinh tien tien)

Ma khoa = 3 so vi tri 4-6 cua MSSV (VD: 2521050285 -> khoa 105).

## Cach chay
### Cach 1 - 1 click
Nhap doi file seed_data.bat

### Cach 2 - Dong lenh
cd D:\CODE\humg-microservices\student-service
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8
set DEBUG=True
python manage.py seed_khoa_nganh_humg

## Reset sach
python manage.py seed_khoa_nganh_humg --clear
CANH BAO: --clear xoa het Khoa/Nganh, sinh vien bi NULL.

## Export / Import fixtures
- Export: nhap doi export_fixtures.bat
- Import: python manage.py loaddata khoa.json + nganh.json

## Danh sach Khoa
| Ma | Ten | So nganh |
|---|---|---|
| 100 | Khoa Khoa hoc co ban | 5 |
| 101 | Khoa Dau khi | 8 |
| 102 | Khoa Dia chat | 9 |
| 103 | Khoa Trac dia - Ban do | 5 |
| 104 | Khoa Mo | 4 |
| 105 | Khoa Cong nghe Thong tin | 3 |
| 106 | Khoa Co - Dien | 9 |
| 107 | Khoa Xay dung | 5 |
| 108 | Khoa Moi truong | 2 |
| 401 | Khoa Kinh te - QTKD | 4 |

Tong: 54 nganh
