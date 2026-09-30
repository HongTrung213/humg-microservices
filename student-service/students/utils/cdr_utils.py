import logging
from datetime import datetime
from django.conf import settings
from django.utils import timezone
import requests

logger = logging.getLogger(__name__)


def get_student_exam_history(sinh_vien_id):
    """Gọi Exam Service để lấy lịch sử thi của sinh viên."""
    try:
        resp = requests.get(
            f'{settings.EXAM_SERVICE_URL}lichsuthi/?sinh_vien_id={sinh_vien_id}',
            timeout=5,
        )
        if resp.status_code == 200:
            return resp.json()
        return []
    except Exception as e:
        logger.warning(f"Exam service failed for SV {sinh_vien_id}: {e}")
        return []


def get_student_certificates(sinh_vien_id):
    """Gọi Certificate Service để lấy danh sách chứng chỉ của sinh viên."""
    try:
        resp = requests.get(
            f'{settings.CERTIFICATE_SERVICE_URL}chungchi/?sinh_vien_id={sinh_vien_id}',
            timeout=5,
        )
        if resp.status_code == 200:
            return resp.json()
        return []
    except Exception as e:
        logger.warning(f"Cert service failed for SV {sinh_vien_id}: {e}")
        return []


def _cert_con_hieu_luc(cert):
    """
    Kiểm tra chứng chỉ còn hiệu lực.
    - Nếu ngay_het_han = None → vĩnh viễn, luôn hợp lệ.
    - Nếu có ngay_het_han → phải >= hôm nay.
    """
    ngay_het_han = cert.get('ngay_het_han')
    if not ngay_het_han:
        return True  # Vĩnh viễn

    try:
        ngay_het = datetime.strptime(ngay_het_han, '%Y-%m-%d').date()
        return ngay_het >= timezone.now().date()
    except (ValueError, TypeError):
        return False


def check_dat_ngoai_ngu(sinh_vien_id, required_bac=3):
    """Kiểm tra sinh viên đạt CĐR Ngoại ngữ."""
    # 1. Kiểm tra điểm thi
    exams = get_student_exam_history(sinh_vien_id)
    for exam in exams:
        if exam.get('mon_thi') == 'CDR_NGOAI_NGU' and exam.get('ket_qua_dat'):
            return True

    # 2. Kiểm tra chứng chỉ (dùng loai='NGOAI_NGU', trang_thai='DAT')
    certs = get_student_certificates(sinh_vien_id)
    for cert in certs:
        danh_muc = cert.get('danh_muc', {})
        if not isinstance(danh_muc, dict):
            continue

        if (cert.get('trang_thai') == 'DAT'
                and danh_muc.get('loai') == 'NGOAI_NGU'
                and danh_muc.get('bac', 0) >= required_bac
                and _cert_con_hieu_luc(cert)):
            return True

    return False


def check_dat_tin_hoc(sinh_vien_id):
    """Kiểm tra sinh viên đạt CĐR Tin học."""
    # 1. Kiểm tra điểm thi
    exams = get_student_exam_history(sinh_vien_id)
    for exam in exams:
        if exam.get('mon_thi') == 'CDR_TIN_HOC' and exam.get('ket_qua_dat'):
            return True

    # 2. Kiểm tra chứng chỉ (dùng loai='TIN_HOC', trang_thai='DAT')
    certs = get_student_certificates(sinh_vien_id)
    for cert in certs:
        danh_muc = cert.get('danh_muc', {})
        if not isinstance(danh_muc, dict):
            continue

        if (cert.get('trang_thai') == 'DAT'
                and danh_muc.get('loai') == 'TIN_HOC'
                and _cert_con_hieu_luc(cert)):
            return True

    return False


def dat_chuan_dau_ra(sinh_vien_id, required_bac=3):
    """Kiểm tra đạt cả hai chuẩn đầu ra."""
    return check_dat_ngoai_ngu(sinh_vien_id, required_bac) and check_dat_tin_hoc(sinh_vien_id)