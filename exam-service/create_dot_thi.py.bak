import os
import requests
import json

# L?y token
token_resp = requests.post(
    'http://localhost:8000/api/token/',
    json={'username': 'admin', 'password': os.getenv('ADMIN_PASSWORD')}
)
token = token_resp.json()['access']
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# T?o d?t thi
data = {
    "ma_dot": "DOT001",
    "ten_dot": "Ð?t thi CÐR Ngo?i ng? tháng 7",
    "loai": "CDR_NN",  # Thêm tru?ng loai (có th? là CDR_NN, CDR_TH, TIN_CHI)
    "ngay_bat_dau": "2026-07-10",
    "ngay_ket_thuc": "2026-07-15",
    "thoi_gian_bat_dau": "2026-07-10T08:00:00Z",
    "thoi_gian_ket_thuc": "2026-07-15T17:00:00Z",
    "diem_chuan_ngoai_ngu": 5.0,
    "diem_liet_ngoai_ngu": 0.0,
    "diem_chuan_tin_hoc": 5.0,
    "diem_liet_tin_hoc": 0.0
}

resp = requests.post('http://localhost:8002/api/dotthi/', json=data, headers=headers)
print(resp.status_code)
print(resp.json())
