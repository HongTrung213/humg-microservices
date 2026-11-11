import pandas as pd
import requests
import re
from datetime import datetime
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import IntegrityError

from .models import LopBoiDuong, DangKyLop, LichHoc
from .serializers import LopBoiDuongSerializer, DangKyLopSerializer, LichHocSerializer


class LopBoiDuongViewSet(viewsets.ModelViewSet):
    queryset = LopBoiDuong.objects.all()
    serializer_class = LopBoiDuongSerializer

    # ========================================================
    # ACTION: IMPORT SINH VIÊN VÀO LỚP (QUY TRÌNH TRUNG TÂM)
    # ========================================================
    @action(detail=True, methods=['post'])
    def import_students(self, request, pk=None):
        """
        Import danh sách sinh viên từ file Excel vào lớp.
        File cần có cột: MSSV (hoặc ma_sv, masv, mã sinh viên)
        Sinh viên được tự động thêm vào lớp với trạng thái DA_DUYET.
        """
        lop = self.get_object()
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'Chưa chọn file Excel'}, status=400)

        try:
            df = pd.read_excel(file)
        except Exception as e:
            return Response({'error': f'Lỗi đọc file: {str(e)}'}, status=400)

        # Chuẩn hóa tên cột
        df.columns = [self._normalize_key(c) for c in df.columns]
        
        # Kiểm tra cột MSSV
        mssv_columns = ['mssv', 'masv', 'masinhvien', 'ma_sv', 'mãsinhviên']
        mssv_col = None
        for col in mssv_columns:
            if col in df.columns:
                mssv_col = col
                break
        
        if not mssv_col:
            return Response({
                'error': 'File phải có cột MSSV (hoặc ma_sv, masv, mã sinh viên)'
            }, status=400)

        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        headers = {'Authorization': f'Bearer {token}'}
        
        created = 0
        existed = 0
        not_found = 0
        errors = []

        for idx, row in df.iterrows():
            mssv = str(row.get(mssv_col, '')).strip()
            if not mssv:
                errors.append(f"Dòng {idx+2}: Thiếu MSSV")
                continue

            # Gọi Student Service để lấy sinh viên
            try:
                resp = requests.get(
                    f'http://localhost:8001/api/sinhvien/?ma_sv={mssv}',
                    headers=headers,
                    timeout=5
                )
                if resp.status_code != 200:
                    errors.append(f"Dòng {idx+2}: Lỗi kết nối Student Service")
                    continue
                    
                data = resp.json()
                if not data:
                    not_found += 1
                    errors.append(f"Dòng {idx+2}: Không tìm thấy SV {mssv}")
                    continue
                    
                sv_data = data[0] if isinstance(data, list) else data
                sv_id = sv_data['id']

                # Tạo đăng ký
                try:
                    dang_ky, is_created = DangKyLop.objects.get_or_create(
                        sinh_vien_id=sv_id,
                        lop=lop,
                        defaults={'trang_thai': 'DA_DUYET'}
                    )
                    
                    if is_created:
                        created += 1
                        # Gửi thông báo
                        self._send_notification(sv_id, lop, request)
                    else:
                        existed += 1
                except IntegrityError:
                    errors.append(f"Dòng {idx+2}: SV {mssv} đã đăng ký lớp này")

            except Exception as e:
                errors.append(f"Dòng {idx+2}: {str(e)}")

        # Cập nhật sĩ số hiện tại
        lop.si_so_hien_tai = DangKyLop.objects.filter(lop=lop, trang_thai='DA_DUYET').count()
        lop.save(update_fields=['si_so_hien_tai'])

        return Response({
            'message': 'Import hoàn tất',
            'created': created,
            'existed': existed,
            'not_found': not_found,
            'errors': errors[:50]
        })

    # ========================================================
    # ACTION: IMPORT LỊCH HỌC (THỜI KHÓA BIỂU)
    # ========================================================
    @action(detail=False, methods=['post'])
    def import_schedule(self, request):
        """
        Import lịch học từ file Excel (hỗ trợ merge cells).
        File cần các cột: Mã MH, Tên môn học, NH, Thứ, Tiết BĐ, Số tiết, Phòng, Thời gian học
        """
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'Chưa chọn file Excel'}, status=400)

        try:
            # Đọc file, header ở dòng thứ 2 (dòng 1 là tiêu đề)
            df = pd.read_excel(file, header=1)
        except Exception as e:
            return Response({'error': f'Lỗi đọc file: {str(e)}'}, status=400)

        # Xử lý merge cells
        df = df.ffill()
        
        # Chuẩn hóa tên cột
        df.columns = [self._normalize_key(str(c)) for c in df.columns]

        # Kiểm tra các cột bắt buộc
        required = ['mamh', 'tenmonhoc', 'nh', 'thu', 'tietbd', 'sotiet', 'phong', 'thoigianhoc']
        missing = [c for c in required if c not in df.columns]
        if missing:
            return Response({
                'error': f'File thiếu các cột: {", ".join(missing)}'
            }, status=400)

        created_count = 0
        errors = []
        class_cache = {}

        for idx, row in df.iterrows():
            try:
                ma_mh = str(row['mamh']).strip()
                if not ma_mh:
                    continue  # Bỏ qua dòng trống
                    
                ten_mon = str(row['tenmonhoc']).strip()
                nhom = str(row['nh']).strip()
                thu = int(row['thu'])
                tiet_bd = int(row['tietbd'])
                so_tiet = int(row['sotiet'])
                phong = str(row['phong']).strip()
                thoi_gian = str(row['thoigianhoc']).strip()
                giang_vien = str(row.get('gv', '')).strip() if 'gv' in row else ''
                so_sv = int(row.get('sosv', 0)) if 'sosv' in row else 0

                # Parse thời gian
                ngay_bd, ngay_kt = self._parse_thoi_gian(thoi_gian)

                # Tìm hoặc tạo lớp
                cache_key = f"{ma_mh}_{nhom}"
                if cache_key not in class_cache:
                    lop = LopBoiDuong.objects.filter(ma_mh=ma_mh, nhom=nhom).first()
                    if not lop:
                        loai = 'NN' if 'tiếng anh' in ten_mon.lower() or 'anh' in ten_mon.lower() else 'TH'
                        lop = LopBoiDuong.objects.create(
                            ma_lop=f"{ma_mh}_{nhom}",
                            ten_lop=f"{ten_mon} - Nhóm {nhom}",
                            loai=loai,
                            so_luong_toi_da=so_sv if so_sv > 0 else 30,
                            bat_dau=ngay_bd,
                            ket_thuc=ngay_kt,
                            trang_thai='OPEN',
                            ma_mh=ma_mh,
                            nhom=nhom
                        )
                    class_cache[cache_key] = lop
                else:
                    lop = class_cache[cache_key]

                # Tạo bản ghi lịch học
                LichHoc.objects.create(
                    lop=lop,
                    thu=thu,
                    tiet_bat_dau=tiet_bd,
                    tiet_ket_thuc=tiet_bd + so_tiet - 1,
                    phong_hoc=phong,
                    giang_vien=giang_vien,
                    ghi_chu=f"Ngày học: {thoi_gian}"
                )
                created_count += 1

            except Exception as e:
                errors.append(f"Dòng {idx+2}: {str(e)}")

        return Response({
            'message': f'Đã tạo {created_count} buổi học cho các lớp',
            'errors': errors[:50]
        })

    # ========================================================
    # HÀM TIỆN ÍCH
    # ========================================================

    def _normalize_key(self, text):
        """Chuẩn hóa tên cột: bỏ dấu, viết thường, bỏ ký tự đặc biệt"""
        text = str(text).lower().strip()
        text = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', text)
        text = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', text)
        text = re.sub(r'[ìíịỉĩ]', 'i', text)
        text = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', text)
        text = re.sub(r'[ùúụủũưừứựửữ]', 'u', text)
        text = re.sub(r'[ỳýỵỷỹ]', 'y', text)
        text = re.sub(r'đ', 'd', text)
        return re.sub(r'[^a-z0-9]', '', text)

    def _parse_thoi_gian(self, text):
        """Parse chuỗi '25/06/2026 – 23/07/2026' thành 2 date"""
        dates = re.findall(r'(\d{2}[/-]\d{2}[/-]\d{4})', text)
        if len(dates) >= 2:
            ngay_bd = datetime.strptime(dates[0], '%d/%m/%Y').date() if '/' in dates[0] else datetime.strptime(dates[0], '%d-%m-%Y').date()
            ngay_kt = datetime.strptime(dates[1], '%d/%m/%Y').date() if '/' in dates[1] else datetime.strptime(dates[1], '%d-%m-%Y').date()
            return ngay_bd, ngay_kt
        return datetime.now().date(), datetime.now().date()

    def _send_notification(self, sv_id, lop, request):
        """Gửi thông báo qua Notification Service"""
        try:
            token = request.headers.get('Authorization', '').replace('Bearer ', '')
            headers = {'Authorization': f'Bearer {token}'}
            
            noi_dung = f"""Bạn đã được thêm vào lớp {lop.ten_lop}.
Mã lớp: {lop.ma_lop}
Loại: {lop.get_loai_display()}
Ngày bắt đầu: {lop.bat_dau}
Ngày kết thúc: {lop.ket_thuc}

Vui lòng xem lịch học trên hệ thống."""
            
            requests.post(
                'http://localhost:8005/api/thongbao/',
                json={
                    'sinh_vien_id': sv_id,
                    'tieu_de': f'Đã được thêm vào lớp {lop.ten_lop}',
                    'noi_dung': noi_dung,
                    'loai': 'ACADEMIC',
                    'is_active': True
                },
                headers=headers,
                timeout=5
            )
        except Exception:
            pass


class DangKyLopViewSet(viewsets.ModelViewSet):
    queryset = DangKyLop.objects.all()
    serializer_class = DangKyLopSerializer

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        """Duyệt hoặc từ chối đăng ký"""
        reg = self.get_object()
        action = request.data.get('action')
        
        if action == 'approve':
            reg.trang_thai = 'DA_DUYET'
        elif action == 'reject':
            reg.trang_thai = 'TU_CHOI'
        else:
            return Response({'error': 'Invalid action. Must be "approve" or "reject"'}, status=400)
        
        reg.save()
        
        # Cập nhật sĩ số
        lop = reg.lop
        lop.si_so_hien_tai = DangKyLop.objects.filter(lop=lop, trang_thai='DA_DUYET').count()
        lop.save(update_fields=['si_so_hien_tai'])
        
        return Response({'status': 'ok', 'trang_thai': reg.trang_thai})


class LichHocViewSet(viewsets.ModelViewSet):
    """CRUD cho lịch học"""
    queryset = LichHoc.objects.all()
    serializer_class = LichHocSerializer
