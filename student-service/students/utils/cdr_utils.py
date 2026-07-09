import requests
from datetime import datetime, timedelta
from django.utils import timezone

def get_student_exam_history(sinh_vien_id):
    """
    Gọi Exam Service để lấy lịch sử thi của sinh viên.
    """
    try:
        resp = requests.get(f'http://localhost:8002/api/lichsuthi/?sinh_vien_id={sinh_vien_id}', timeout=5)
        if resp.status_code == 200:
            return resp.json()
        return []
    except Exception:
        return []

def get_student_certificates(sinh_vien_id):
    """
    Gọi Certificate Service để lấy danh sách chứng chỉ của sinh viên.
    """
    try:
        resp = requests.get(f'http://localhost:8003/api/chungchi/?sinh_vien_id={sinh_vien_id}', timeout=5)
        if resp.status_code == 200:
            return resp.json()
        return []
    except Exception:
        return []

def check_dat_ngoai_ngu(sinh_vien_id, required_bac=3):
    """
    Kiểm tra sinh viên đạt CĐR Ngoại ngữ hay chưa.
    - Dựa trên chứng chỉ hợp lệ (còn hiệu lực) hoặc điểm thi đạt.
    """
    exams = get_student_exam_history(sinh_vien_id)
    # Lọc điểm thi CĐR Ngoại ngữ đạt
    for exam in exams:
        if exam.get('mon_thi') == 'CDR_NGOAI_NGU' and exam.get('ket_qua_dat'):
            # Kiểm tra thời hạn hiệu lực (mặc định 60 tháng)
            ngay_cap = exam.get('ngay_cap_nhat')
            if ngay_cap:
                ngay_cap = datetime.fromisoformat(ngay_cap.replace('Z', '+00:00'))
                if timezone.now() - ngay_cap < timedelta(days=60*30):
                    return True

    # Kiểm tra chứng chỉ hợp lệ
    certs = get_student_certificates(sinh_vien_id)
    for cert in certs:
        if cert.get('trang_thai') == 'DAT' and cert.get('danh_muc', {}).get('loai') == 'NGOAI_NGU':
            # Kiểm tra bậc
            bac = cert.get('danh_muc', {}).get('bac', 0)
            if bac >= required_bac:
                ngay_cap = cert.get('ngay_cap')
                if ngay_cap:
                    ngay_cap = datetime.strptime(ngay_cap, '%Y-%m-%d').date()
                    if timezone.now().date() - ngay_cap < timedelta(days=60*30):
                        return True

    return False

def check_dat_tin_hoc(sinh_vien_id):
    """
    Kiểm tra sinh viên đạt CĐR Tin học hay chưa.
    - Dựa trên chứng chỉ hợp lệ hoặc điểm thi đạt.
    """
    exams = get_student_exam_history(sinh_vien_id)
    for exam in exams:
        if exam.get('mon_thi') == 'CDR_TIN_HOC' and exam.get('ket_qua_dat'):
            ngay_cap = exam.get('ngay_cap_nhat')
            if ngay_cap:
                ngay_cap = datetime.fromisoformat(ngay_cap.replace('Z', '+00:00'))
                if timezone.now() - ngay_cap < timedelta(days=60*30):
                    return True

    certs = get_student_certificates(sinh_vien_id)
    for cert in certs:
        if cert.get('trang_thai') == 'DAT' and cert.get('danh_muc', {}).get('loai') == 'TIN_HOC':
            ngay_cap = cert.get('ngay_cap')
            if ngay_cap:
                ngay_cap = datetime.strptime(ngay_cap, '%Y-%m-%d').date()
                if timezone.now().date() - ngay_cap < timedelta(days=60*30):
                    return True

    return False

def dat_chuan_dau_ra(sinh_vien_id, required_bac=3):
    """
    Kiểm tra sinh viên đạt cả hai chuẩn đầu ra.
    """
    return check_dat_ngoai_ngu(sinh_vien_id, required_bac) and check_dat_tin_hoc(sinh_vien_id)