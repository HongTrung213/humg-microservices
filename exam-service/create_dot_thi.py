import requests
import json

# Lấy token
token_resp = requests.post(
    'http://localhost:8000/api/token/',
    json={'username': 'admin', 'password': '123qwe'}
)
token = token_resp.json()['access']
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# Tạo đợt thi
data = {
    "ma_dot": "DOT001",
    "ten_dot": "Đợt thi CĐR Ngoại ngữ tháng 7",
    "loai": "CDR_NN",  # Thêm trường loai (có thể là CDR_NN, CDR_TH, TIN_CHI)
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