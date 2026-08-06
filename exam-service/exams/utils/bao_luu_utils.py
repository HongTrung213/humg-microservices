from exams.models import BaoLuuDiem
from datetime import timedelta
from django.utils import timezone

def tao_bao_luu_tu_lich_su_thi(sinh_vien_id, dot_thi, loai, 
                               diem_1=None, diem_2=None, diem_3=None, diem_4=None, 
                               nguong=25):
    """
    Tạo bảo lưu điểm cho ngoại ngữ hoặc tin học.
    - loai: 'NN' hoặc 'TH'
    - Ngưỡng mặc định 25 (thang 100). Có thể điều chỉnh theo thực tế.
    - Thời hạn bảo lưu: NN=24 tháng, TH=12 tháng.
    """
    # Xác định phần đạt
    phan_dat = []
    diem_map = {}
    
    if diem_1 is not None and diem_1 >= nguong:
        phan_dat.append('1')
        diem_map['1'] = diem_1
    if diem_2 is not None and diem_2 >= nguong:
        phan_dat.append('2')
        diem_map['2'] = diem_2
    if diem_3 is not None and diem_3 >= nguong:
        phan_dat.append('3')
        diem_map['3'] = diem_3
    if diem_4 is not None and diem_4 >= nguong:
        phan_dat.append('4')
        diem_map['4'] = diem_4
    
    if not phan_dat:
        return None
    
    # Tổng điểm bảo lưu
    tong_bao_luu = sum(diem_map.values())
    
    # Tính thời hạn
    if loai == 'NN':
        thang_het_han = 24
    else:  # TH
        thang_het_han = 12
    
    ngay_het_han = timezone.now().date() + timedelta(days=thang_het_han * 30)
    
    # Tạo hoặc cập nhật bản ghi bảo lưu
    bao_luu, created = BaoLuuDiem.objects.update_or_create(
        sinh_vien_id=sinh_vien_id,
        dot_thi=dot_thi,
        loai=loai,
        defaults={
            'diem_phan_1': diem_map.get('1'),
            'diem_phan_2': diem_map.get('2'),
            'diem_phan_3': diem_map.get('3'),
            'diem_phan_4': diem_map.get('4'),
            'danh_sach_phan': ','.join(phan_dat),
            'diem_bao_luu': tong_bao_luu,
            'ngay_het_han': ngay_het_han,
            'trang_thai': 'ACTIVE'
        }
    )
    return bao_luu


def kiem_tra_bao_luu_het_han():
    """Cập nhật trạng thái bảo lưu hết hạn (chạy cronjob hàng ngày)"""
    from django.utils import timezone
    expired = BaoLuuDiem.objects.filter(
        trang_thai='ACTIVE',
        ngay_het_han__lt=timezone.now().date()
    )
    expired.update(trang_thai='EXPIRED')
    return expired.count()