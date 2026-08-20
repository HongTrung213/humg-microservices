import os
import requests
import time
import json

BASE_URL = 'http://localhost:8000'
STUDENT_URL = 'http://localhost:8001'
EXAM_URL = 'http://localhost:8002'
REPORT_URL = 'http://localhost:8007'

# 1. Lấy token
def get_token():
    resp = requests.post(f'{BASE_URL}/api/token/', json={'username': 'admin', 'password': os.getenv('ADMIN_PASSWORD')})
    return resp.json()['access']

token = get_token()
headers = {'Authorization': f'Bearer {token}'}

print("✅ Token lấy thành công")

# 2. Import sinh viên
print("\n📥 Import sinh viên...")
with open('D:/students.xlsx', 'rb') as f:
    resp = requests.post(f'{STUDENT_URL}/api/import-students/', files={'file': f}, headers=headers)
print(f"   Status: {resp.status_code}, Response: {resp.json()}")

# 3. Kiểm tra danh sách sinh viên
print("\n📋 Danh sách sinh viên:")
resp = requests.get(f'{STUDENT_URL}/api/sinhvien/', headers=headers)
students = resp.json()
print(f"   Tổng số: {len(students)} sinh viên")
for sv in students[:3]:
    print(f"   - {sv['ma_sv']}: {sv['ho_ten']}")

# 4. Import điểm thi
print("\n📥 Import điểm CĐR Ngoại ngữ...")
with open('D:/cdr_nn.xlsx', 'rb') as f:
    resp = requests.post(f'{EXAM_URL}/api/import-exam-scores/', 
                         data={'dot_thi_id': '1', 'loai': 'cdr_nn'},
                         files={'file': f}, headers=headers)
print(f"   Status: {resp.status_code}, Response: {resp.json()}")

# 5. Kiểm tra CĐR sinh viên
print("\n✅ Kiểm tra CĐR từng sinh viên:")
for sv in students[:5]:
    sv_id = sv['id']
    resp = requests.get(f'{STUDENT_URL}/api/sinhvien/{sv_id}/cdr-status/', headers=headers)
    data = resp.json()
    print(f"   {sv['ma_sv']} - CĐR NN: {data['check_dat_ngoai_ngu']}, TH: {data['check_dat_tin_hoc']}, Đạt: {data['dat_chuan_dau_ra']}")

# 6. Xem báo cáo Dashboard
print("\n📊 Dashboard:")
resp = requests.get(f'{REPORT_URL}/api/reports/dashboard/', headers=headers)
dashboard = resp.json()
print(f"   Tổng SV: {dashboard['tong_sinh_vien']}")
print(f"   Đạt CĐR: {dashboard['dat_chuan_dau_ra']} ({dashboard['ti_le_dat_cdr']}%)")
print(f"   Cảnh báo: {dashboard['so_luong_canh_bao']} sinh viên")

# 7. Export Excel báo cáo
print("\n📊 Xuất Excel báo cáo:")
resp = requests.get(f'{REPORT_URL}/api/reports/export-chua-dat-chuan/', headers=headers)
if resp.status_code == 200:
    with open('bao_cao_chua_dat.xlsx', 'wb') as f:
        f.write(resp.content)
    print("   ✅ Đã lưu file bao_cao_chua_dat.xlsx")
else:
    print(f"   ❌ Lỗi: {resp.status_code}")

print("\n✅ Kiểm thử hoàn tất!")