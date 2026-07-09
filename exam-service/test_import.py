import requests

# Lấy token
token_resp = requests.post(
    'http://localhost:8000/api/token/',
    json={'username': 'admin', 'password': '123qwe'}
)
token = token_resp.json()['access']

# Import lịch thi
url = 'http://localhost:8002/api/import-exam-schedule/'
files = {'file': open('D:/lich_thi.xlsx', 'rb')}
data = {'dot_thi_id': '1', 'mon_thi': 'CDR_NGOAI_NGU'}
headers = {'Authorization': f'Bearer {token}'}

resp = requests.post(url, data=data, files=files, headers=headers)
print(resp.json())