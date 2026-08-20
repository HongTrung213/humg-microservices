import os
import requests

# Lấy token
token_resp = requests.post(
    'http://localhost:8000/api/token/',
    json={'username': 'admin', 'password': os.getenv('ADMIN_PASSWORD')}
)
if token_resp.status_code != 200:
    print("Lỗi lấy token:", token_resp.text)
    exit()
token = token_resp.json()['access']
headers = {'Authorization': f'Bearer {token}'}

# Import sinh viên
files = {'file': open('D:/students.xlsx', 'rb')}
resp = requests.post('http://localhost:8001/api/import-students/', files=files, headers=headers)

# Debug: in ra status và raw content
print("Status:", resp.status_code)
print("Raw content:", resp.text[:500])  # In 500 ký tự đầu

if resp.status_code == 200:
    print("Response JSON:", resp.json())
else:
    print("Lỗi:", resp.text)