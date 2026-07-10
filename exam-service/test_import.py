import requests

# Lấy token
token_resp = requests.post(
    'http://localhost:8000/api/token/',
    json={'username': 'admin', 'password': '123qwe'}
)
if token_resp.status_code != 200:
    print("Lỗi lấy token:", token_resp.text)
    exit()
token = token_resp.json()['access']
print("Token:", token)

# Import lịch thi
url = 'http://localhost:8002/api/import-exam-schedule/'
headers = {'Authorization': f'Bearer {token}'}
data = {'dot_thi_id': '1', 'mon_thi': 'CDR_NGOAI_NGU'}
files = {'file': open('D:/lich_thi.xlsx', 'rb')}

resp = requests.post(url, data=data, files=files, headers=headers)
print("Status:", resp.status_code)
print("Response:", resp.json())